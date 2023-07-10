from rest_framework import serializers
from .models import *
from customer_app.models import Customer
from customer_app.serializer import CustomerSerializer
from products_app.serializer import ProductSerializer
from products_app.models import Product
import logging
logger=logging.getLogger(__name__)


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model=Cart
        fields='__all__'
