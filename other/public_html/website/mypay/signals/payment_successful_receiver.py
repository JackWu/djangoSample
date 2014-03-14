from paypal.standard.ipn.signals import payment_was_successful
import logging

def show_me_the_money(sender, **kwargs):
  log = logging.getLogger("dev.ttagit.logger")
  log.debug("SIGNAL!!!!!---Successful Payment")

payment_was_successful.connect(show_me_the_money)
