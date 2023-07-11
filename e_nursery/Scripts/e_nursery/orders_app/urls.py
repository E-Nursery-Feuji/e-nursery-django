from django.urls import path
from .import views

urlpatterns = [
      path('savecart/',views.createCart),
      path('cart/<str:id>/',views.cart),


]
