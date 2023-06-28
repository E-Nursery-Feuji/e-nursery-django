from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'role')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        print(instance)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


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
