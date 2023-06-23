
from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields='__all__'
    

class TypeSerializer():
    class Meta:
        model=Type
        fields='__all__'

class ProductSerializer():
    class Meta:
        model=Product
        fields='__all__'