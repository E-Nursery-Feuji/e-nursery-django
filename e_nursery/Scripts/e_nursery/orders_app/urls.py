from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo),
    path('getallpayments/',views.getAllPaymentstatus),
    path('savepayment/',views.savePayment)
    ]