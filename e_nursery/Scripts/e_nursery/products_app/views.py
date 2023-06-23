from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializer import ImageSerializer
import base64
# Create your views here.

def demo(request):
    return HttpResponse('product app')

@csrf_exempt
def image(request,id=0):
    if request.method=='GET':
        if id==0:
           images=Image.objects.all()
           images_serializer=ImageSerializer(images,many=True)
        else:
            image=Image.objects.get(id=id)
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
