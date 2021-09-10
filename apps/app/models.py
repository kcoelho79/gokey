# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Serial(models.Model):
    serial = models.CharField(max_length=20)
    def __str__(self):
        return self.serial

class Resident(models.Model):
	name = models.CharField(max_length=20)
	serial = models.OneToOneField(Serial, on_delete=models.CASCADE, primary_key=True)

	def __str__(self):
		return self.serial

