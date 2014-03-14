from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
		url(r'^test/', 'mypay.views.test', name='test'),
		url(r'^money-ipn/', 'mypay.views.view_ask_money_ipn', name='money-ipn'),
		url(r'^money-subscribe', 'mypay.views.do_subscribe', name='money-subscribe'),
		url(r'^success', 'mypay.views.success', name='success'),
		url(r'^pay-on-site', 'mypay.views.buy_on_my_site', name='pay-on-site'),
		url(r'^pay-now', 'mypay.views.pay_now', name='pay_now'),
		url(r'^purchase-thanks/$', 'mypay.views.purchase_thanks', name='pay_success'),
		url(r'^purchase-cancelled/$', 'mypay.views.purchase_thanks', name='pay_cancel'),

)
#3f2cf0fe3d994fb8dfe6d8f9g2h5
urlpatterns += patterns('',
	(r'^3f2cf0fe3d994fb8dfe6d8f9g2h5', include('paypal.standard.ipn.urls')),
	(r'^paypal/pdt/', include('paypal.standard.pdt.urls')),
)
