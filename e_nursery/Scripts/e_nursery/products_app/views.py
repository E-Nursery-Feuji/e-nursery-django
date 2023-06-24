from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializer import *
import logging
# Create your views here.

def demo(request):
    return HttpResponse('product app')

@csrf_exempt
def image(request,id=0):
    if request.method=='GET':
        logging.info("GET method")
        if id==0:
           images=Image.objects.all()
           images_serializer=ImageSerializer(images,many=True)
           logging.info("getting all images")
        else:
            image=Image.objects.get(id=id)
            logging.info("getting image by")
            images_serializer=ImageSerializer(image)
        return JsonResponse(images_serializer.data,safe=False)    
    elif request.method=='POST':
      
        image_data = JSONParser().parse(request)
        image_serializer=ImageSerializer(data=image_data)
        if image_serializer.is_valid():
            image_serializer.save()
            return JsonResponse("Saved successfully...",safe=False)
        return JsonResponse("failed to save..",safe=False)
    
    elif request.method=='PUT':
        image_data=JSONParser().parse(request)
        image=Image.objects.get(id=image_data['id'])
        image_serializer=ImageSerializer(image,data=image_data)
        if image_serializer.is_valid():
            image_serializer.save()
            return JsonResponse("UPDATED successfully...",safe=False)
        return JsonResponse("failed to save..",safe=False)
    elif request.method=='DELETE':
        image=Image.objects.get(id=id)
        image.delete()
        return JsonResponse("deleted successfully",safe=False)
    

@csrf_exempt
def type(request,id=0):
    if request.method=='GET':
        if id==0:
           types=Type.objects.all()
           types_serializer=TypeSerializer(types,many=True)
        else:
            type=Type.objects.get(id=id)
            types_serializer=TypeSerializer(type)
        return JsonResponse(types_serializer.data,safe=False)    
    elif request.method=='POST':
      
        type_data = JSONParser().parse(request)
        type_serializer=TypeSerializer(data=type_data)
        if type_serializer.is_valid():
            type_serializer.save()
            return JsonResponse("Saved successfully...",safe=False)
        return JsonResponse("failed to save..",safe=False)
    
    elif request.method=='PUT':
        type_data=JSONParser().parse(request)
        type=Type.objects.get(id=type_data['id'])
        type_serializer=TypeSerializer(type,data=type_data)
        if type_serializer.is_valid():
            type_serializer.save()
            return JsonResponse("UPDATED successfully...",safe=False)
        return JsonResponse("failed to save..",safe=False)
    elif request.method=='DELETE':
        type=Type.objects.get(id=id)
        type.delete()
        return JsonResponse("deleted successfully",safe=False)


@csrf_exempt
def product(request,id=0):
    if request.method=='GET':
        if id==0:
           products=Product.objects.all()
           products_serializer=ProductSerializer(products,many=True)
        else:
            product=Product.objects.get(id=id)
            products_serializer=ProductSerializer(product)
        return JsonResponse(products_serializer.data,safe=False) 
       
    elif request.method=='POST':    
        product_data = JSONParser().parse(request)
        product_serializer=ProductSerializer(data=product_data)
       
        if product_serializer.is_valid():
                product_serializer.save()
                return JsonResponse("Saved successfully...",safe=False)
    
        return JsonResponse(product_serializer.errors,safe=False)
        
       
    
    elif request.method=='PUT':
        product_data=JSONParser().parse(request)
       
        product=Product.objects.get(id=product_data['id'])
        product_serializer=ProductSerializer(product,data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("UPDATED successfully...",safe=False)
        return JsonResponse(product_serializer.errors,safe=False)
    
    
    elif request.method == 'DELETE':
        product = Product.objects.get(id=id)
        image = product.image  # Retrieve the image associated with the product
        product.delete()  # Delete the product
        image.delete()  # Delete the associated image
        return JsonResponse("Deleted successfully", safe=False)
