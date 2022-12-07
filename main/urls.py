from django.urls import path, include
from .views import HomeView, About, ContactUs


urlpatterns = [
		path('',HomeView,name='home'),
		path('about-us/',About,name='about'),
		path('contact-us',ContactUs,name='contact')
]