from django.urls import path
from . import views

urlpatterns = [
    path('deliveries/',views.getToDeliveries),
    path('deliveries/<int:id>/',views.getToDeliveries),
    path('savedelivery/',views.createDelivery),
    path('updatedelivery/<int:id>/',views.updateDelivery),
    path('deletedelivery/<int:id>/',views.deleteDelivery),

    path('payments/',views.getPayments),
    path('payments/<int:id>/',views.getPayments),
    path('savepayment/',views.createPayment),
    path('updatepayments/<int:id>/',views.updatePayment),
    path('deletepayment/<int:id>/',views.deletePayment),

    path('cart/',views.getCart),
    path('cart/<int:id>/',views.getCart),
    path('savecart/',views.createCart),
    path('updatecart/<int:id>/',views.updateCart),
    path('deletecart/<int:id>/',views.deleteCart),





   
]