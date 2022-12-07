from django.urls import path, include
from rest_framework import routers
from . import views
from .views import RechargeView, transactions, PhoneRecharge



router = routers.DefaultRouter()
router.register(r'recharge', views.RechargeView)


urlpatterns = [
   
    path('recharge/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('transaction/', transactions.as_view(), name='transaction'),
    path('recharge-now/', PhoneRecharge.as_view(), name='prerecharge'),

]
