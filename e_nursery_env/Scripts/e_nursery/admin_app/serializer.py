from rest_framework import serializers
from .models import *

class AdminModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields = ('id', 'first_name', 'last_name', 'email', 'password','role','status')

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