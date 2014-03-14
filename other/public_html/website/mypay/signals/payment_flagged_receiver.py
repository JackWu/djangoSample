from django.db import models
from paypal.standard.ipn.signals import payment_was_flagged
import logging

def flagged_signal(sender, **kwargs):
  log = logging.getLogger("dev.ttagit.logger")
  log.debug("SIGNAL!!!!-----FLAGGED SIGNAL")

payment_was_flagged.connect(flagged_signal)
