from paypal.standard.ipn.signals import subscription_cancel
import logging

def sub_cancel_receiver(sender, **kwargs):
  log = logging.getLogger("dev.ttagit.logger")
	log.debug("SIGNAL!!!!----Cancel Subscription")

subscription_cancel.connect(show_me_the_money)
