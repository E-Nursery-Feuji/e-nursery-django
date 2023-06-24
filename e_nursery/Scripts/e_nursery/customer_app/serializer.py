# created by Priya Patel & Samundar Singh Rathore
from rest_framework import serializers
from .models import *

# for the database table & serialize the object
class CustomerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__' #include all the fields of customer model

#for Users table 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields='__all__'

#for login the data
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields = ('email', 'password')