from paypal.standard.ipn.signals import subscription_signup
import logging

def sub_signup_receiver(sender, **kwargs):
  log = logging.getLogger("dev.ttagit.logger")
  log.debug("SIGNAL!!!!----Signup Subscr")

subscription_signup.connect(sub_signup_receiver)
