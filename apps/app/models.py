# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
import api.libbit as convert

class Resident(models.Model):
	name = models.CharField(max_length=20)
	serial = models.CharField(max_length=9)

	def get_absolute_url(self):
		return '/'

	def __str__(self):
		return self.serial

def serial_to_hex(sender, instance, *args, **kwargs):
	h = convert.serial_to_strhex(instance.serial)
	instance.serial = h
pre_save.connect(serial_to_hex, sender=Resident)

