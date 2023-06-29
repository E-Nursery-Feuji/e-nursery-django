
from rest_framework import serializers
from .models import *
from customer_app.models import Customer
from customer_app.serializer import CustomerModelSerializer
from products_app.serializer import ProductSerializer
from products_app.models import Product
import logging
logger=logging.getLogger(__name__)

class Delivery_statusSerializer(serializers.ModelSerializer):
    class Meta:
        model=DeliveryStatus
        fields='__all__'
    

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'


class CartSerializer(serializers.ModelSerializer):
    customer = CustomerModelSerializer(read_only=False)
    products = ProductSerializer(read_only=False)

    class Meta:
        model=Cart
        fields='__all__'

    def create(self, validated_data):
        Customer_data = validated_data.pop('customer')
        product_data = validated_data.pop('products')
     
        
        customer = Customer.objects.filter(**Customer_data).first()
        product = Product.objects.filter(**product_data).first()


        product = Cart.objects.create(customer=customer, product=product, **validated_data)
        return product
        


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
