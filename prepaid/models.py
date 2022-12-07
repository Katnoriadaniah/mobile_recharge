from django.db import models
from django.urls import reverse

# Create your models here.
class recharge(models.Model):
	Phonenumber = models.CharField(max_length=12)
	Serviceprovider = models.CharField(max_length=55)
	Plan = models.CharField(max_length=255)

	def __str__(self):
		return self.Phonenumber

	def get_absolute_url(self):
		return reverse('transaction')