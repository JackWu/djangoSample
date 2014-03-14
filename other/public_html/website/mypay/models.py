from django.db import models
from paypal.standard.ipn.signals import subscription_cancel
import logging

def show_me_cancel(sender, **kwargs):
	logger = logging.getLogger("dev.ttagit.logger")
	logger.info("subscription_cancel")

subscription_cancel.connect(show_me_cancel)
