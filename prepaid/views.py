from django.shortcuts import render
from rest_framework import viewsets
from .serializers import registerserializer
from .models import recharge
import requests
from django.shortcuts import render
from django.views.generic import ListView, CreateView



class RechargeView(viewsets.ModelViewSet):
	queryset = recharge.objects.all().order_by('Phonenumber')
	serializer_class = registerserializer

class transactions(ListView):
	model = recharge
	template_name = 'recharge/transaction.html'

class PhoneRecharge(CreateView):
	model = recharge
	template_name = 'recharge/recharge.html'
	fields = '__all__'
