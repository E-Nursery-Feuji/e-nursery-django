
from rest_framework import serializers
from .models import *
import logging
logger=logging.getLogger(__name__)

class Delivery_statusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Delivery_status
        fields='__all__'
    

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'

