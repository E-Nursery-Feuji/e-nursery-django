from django.urls import path
from . import views
from .views import *

# created by Priya Patel & Samundar Singh Rathore

urlpatterns = [
    # path('',views.demo ),
    path('save/',saveCustomer,name='savecustomer'),
    path('signin/',login,name='login')
]