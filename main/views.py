from django.shortcuts import render

# Create your views here.
from django.shortcuts import render



def HomeView(request):
	return render(request, 'home.html')

def About(request):
	return render(request, 'about_us.html')

def ContactUs(request):
	return render(request, 'contact_us.html')