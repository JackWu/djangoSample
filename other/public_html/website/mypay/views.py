# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from paypal.standard.forms import PayPalPaymentsForm
from paypal.pro.views import PayPalPro
from django.template import RequestContext
from decimal import *



import models
import util_paypal
import logging

log = logging.getLogger("dev.ttagit.logger")


def test(request):
	return render_to_response('test.html')

def view_ask_money_ipn(request):
	# What you want the button to do.
	paypal_dict = {
			"business":settings.PAYPAL_RECEIVER_EMAIL,
			"amount":"0.01",
			"item_name":"Ttagit Pro Account",
			"invoice":"unique-invoice-id",
			"notify_url":"http://dev.ttagit.com/paypal-ipn",
			"return_url":"http://dev.ttagit.com/paypal/pdt/",
			"cancel_return":"",
	}

	form = PayPalPaymentsForm(initial=paypal_dict)
	context = {"form":form.sandbox()}
	return render_to_response("payment.html", context)

def do_subscribe(request):
	log.info("mypal module -> view.py -> do_subscribe()")
	paypal_dict={
		"cmd":"_xclick-subscriptions",
		"business":settings.PAYPAL_RECEIVER_EMAIL,
		"a3":"0.01",
		"p1":1,
		"p2":1,
		"p3":1,
		"t3":"D",
		"src":"1",
		"sra":"1",
		"no_note":"1",
		"item_name":"ttagit_pro_market",
    #use item_number for user id
		"item_number":"4ffb5e1a0cf2c9e46dda6810",
		"notify_url":"https://dev.ttagit.com/3f2cf0fe3d994fb8dfe6d8f9g2h5",
		"return_url":"https://dev.ttagit.com/paypal/pdt/",
		"cancel_return":"https://dev.ttagit.com/cancel",
	}
	form = PayPalPaymentsForm(initial=paypal_dict, button_type="subscribe")
	context = {"form":form.sandbox()}
	return render_to_response("payment.html", context)

def success(request):
    #resource = get_object_or_404( models.Resource, pk=id )
    #user = get_object_or_404( User, pk=uid )
    if request.REQUEST.has_key('tx'):
      tx = request.REQUEST['tx']
      try:
        existing = models.Purchase.objects.get( tx=tx )
        return render_to_response('error.html', { 'error': "Duplicate transaction" }, context_instance=RequestContext(request) )
      except models.Purchase.DoesNotExist:
        result = util_paypal.Verify( tx )
        if result.success() and Decimal('0.01') == result.amount(): # valid
          purchase = models.Purchase(tx=tx, amount=request.REQUEST['amt'], status=request.REQUEST['st'], cc=request.REQUEST['cc'], 
item_number=request.REQUEST['item_number'])
          purchase.save()
          return render_to_response('success.html', context_instance=RequestContext(request) )
        else: # didn't validate
          return render_to_response('error.html', { 'error': "Failed to validate payment" }, context_instance=RequestContext(request) )
    else: # no tx
      return render_to_response('error.html', { 'error': "No transaction specified" }, context_instance=RequestContext(request) )

@csrf_exempt
def buy_on_my_site(request):
	log.info("Beginning of buy_on_my_site")
	item = {"amt": "0.01",
					"inv":"inventory",
					"custom":"tracking",
					"cancelurl":"https://dev.ttagit.com/cancel",
					"returnurl":"https://dev.ttagit.com/paypal/pdt/"}
	kw = {"item":item,
				"payment_template":"pro/payment.html",
				"confirm_template":"pro/confirmation.html",
				"success_url":"https://dev.ttagit.com/paypal/pdt/"}
	ppp = PayPalPro(**kw)
	return ppp(request)

@csrf_exempt
def pay_now( request ):
    # Override django-paypal library endpoints to include 'useraction=commit'
    # which changed PayPal's review page to be a 'pay now' page.
    # This is ugly but I didn't want to subclass.
    from paypal.pro import views as pro_views
    pro_views.EXPRESS_ENDPOINT = "https://www.paypal.com/webscr?cmd=_express-checkout&useraction=commit&%s"
    pro_views.SANDBOX_EXPRESS_ENDPOINT = "https://www.sandbox.paypal.com/webscr?cmd=_express-checkout&useraction=commit&%s"

    # ...because we use 'useraction=commit', there's no need to show the confirm page.
    # So let's change the request to show the confirmation form into a request to
    # approve it. It just so happens that the arguments are the same -- the difference
    # is between the GET and the POST.
    # <input type="hidden" name="token" value="EC-485941126E653491T" id="id_token"/>
    # <input type="hidden" name="PayerID" value="78W69D3FEVWJBC" id="id_PayerID"/>
    if request.method == 'GET' and 'token' in request.GET and 'PayerID' in request.GET:
        request.method = 'POST'
        request.POST = request.GET # Crudely convert GET to POST

    item = {
        'amt':           99.99, # Amount to charge for item
        'currencycode':  'usd',
        #'inv':           1, # Unique tracking variable paypal - must be a number.
        #'desc':          'Your product name', # Deprecated by PayPal, don't bother
                                               # (you'll get the name twice in your statement otherwise)
        'custom':        'custom1', # Custom tracking variable for you. Realistically you have to pass
                                    # this if you're specifying basket contents to PayPal as django-paypal
                                    # won't be given `item_name` in the IPN, only `item_name1` etc.
                                    # which it cannot interpret.
        'cancelurl':     'http://%s%s' % (DYNAMIC_URL, reverse('pay_cancel')), # Express checkout cancel url
        'returnurl':     'http://%s%s' % (DYNAMIC_URL, reverse('pay_now')), # Express checkout return url
        'allownote':     0, # Disable "special instructions for seller"
        'l_name0':       'Your product name',
        #'l_number0':    1234,
        #'l_desc0':      'longer description',
        'l_amt0':        99.99,
        'l_qty0':        1,
        'itemamt':       99.99,
        #'taxamt':       0.00,
        #'shippingamt':  0.00,
        #'handlingamt':  0.00,
        #'shipdiscamt':  0.00,
        #'insuranceamt': 0.00,
    }

    kw = {
        'item': item,
        'payment_template': 'cms/register.html', # Template name for payment
        'confirm_template': 'cms/paypal-confirmation.html', # Template name for confirmation
        'success_url':      reverse('pay_success'), # Ultimate return URL
    }

    ppp = PayPalPro(**kw)
    return ppp(request)

