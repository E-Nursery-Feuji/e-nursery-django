from django.urls import path

from .views import *

# created by Priya Patel & Samundar Singh Rathore

urlpatterns = [
   
    path('save/',saveCustomer,name='savecustomer'),
    path('signin/',login,name='login')
]