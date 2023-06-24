
from rest_framework import serializers
from .models import *
import logging
logger=logging.getLogger(__name__)

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields='__all__'
    

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Type
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=False)
    type = TypeSerializer(read_only=False)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        image_data = validated_data.pop('image')
        type_data = validated_data.pop('type')
     
        image = Image.objects.create(**image_data)
        type = Type.objects.filter(**type_data).first()
        if not type:
            type = Type.objects.create(**type_data)

        product = Product.objects.create(image=image, type=type, **validated_data)
        return product
    
    def update(self, instance, validated_data):
        image_data = validated_data.pop('image', None)
        type_data = validated_data.pop('type', None)

        if image_data:
            image_serializer = ImageSerializer(instance.image, data=image_data)
            if image_serializer.is_valid():
                image_serializer.save()
            else:
                raise serializers.ValidationError(image_serializer.errors)

        if type_data:
            type_serializer = TypeSerializer(instance.type, data=type_data)
            if type_serializer.is_valid():
                type_serializer.save()
            else:
                raise serializers.ValidationError(type_serializer.errors)

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()

        return instance