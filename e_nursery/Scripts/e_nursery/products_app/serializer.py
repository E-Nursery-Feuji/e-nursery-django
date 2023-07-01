
from rest_framework import serializers
from .models import *
import logging as log

#for the log level & file & formate
log.basicConfig(filename='e_nursery_log.log', level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
        image = Image.objects.filter(**image_data).last()
        type = Type.objects.filter(**type_data).first()
        if not type:
            type = Type.objects.create(**type_data)
            image = Image.onjects.create(**image_data)

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

        # if type_data:
        #     type_serializer = TypeSerializer(instance.type, data=type_data)
        #     if type_serializer.is_valid():
        #         type_serializer.save()
        #     else:
        #         raise serializers.ValidationError(type_serializer.errors)

        instance.type =  Type.objects.filter(**type_data).first()
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()

        return instance
    

class BlogSerializer(serializers.ModelSerializer):

    image = ImageSerializer(read_only=False)

    class Meta:
        model = Blog
        fields = '__all__'

    def create(self, validated_data):
        image_data = validated_data.pop('image')
        
     
        image = Image.objects.create(**image_data)
     

        blog = Blog.objects.create(image=image,  **validated_data)
        return blog
    
    def update(self, instance, validated_data):
        image_data = validated_data.pop('image', None)

        if image_data:
            image_serializer = ImageSerializer(instance.image, data=image_data)
            if image_serializer.is_valid():
                image_serializer.save()
            else:
                raise serializers.ValidationError(image_serializer.errors)


        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.uploaded_by = validated_data.get('uploaded_by', instance.uploaded_by)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance