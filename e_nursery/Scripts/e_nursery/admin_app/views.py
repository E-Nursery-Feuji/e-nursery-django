from django.shortcuts import render
from django.http import HttpResponse
from customer_app.models import *

from rest_framework import status

from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging as log

# Create your views here.

def demo(request):
    return HttpResponse('admin app')



#for the log level & file & formate
log.basicConfig(filename='e_nursery_log.log', level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') 


# created by Priya Patel & Samundar Singh & Haritha 
# Create your views here.

# for save the customer
@api_view(['POST'])
def saveAdmin(request):
    log.info("saveAdminfunation is started")
    serializer=AdminModelSerializer(data=request.data) #serialize the data
    if serializer.is_valid(): #checing data is valid or not
        log.info("Data is Valid")
        email=request.data.get('email') #get email from request data
        log.info("Checking Email exits")
        data_exist=Users.objects.filter(email=email).exists() #check email is present or not
        if data_exist:
            log.info("Email exist")
            return Response("present") #email present then reponse
        else:
            log.info("Email not exist")
            serializer.save() #email is not present then save the data
            log.info("Data is saved")
            return Response(serializer.data) #after save the data the response
    else:
        log.error("Data is not valid")
        return Response(serializer.errors)


@api_view(['GET'])
def getAdmin(request, id=None):
    if id is not None:
        try:
            
            admin = Admin.objects.get(id=id)
            serializer = AdminModelSerializer(admin)  
            return Response(serializer.data)
        except Admin.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        qs = Admin.objects.all()
        serializer = AdminModelSerializer(qs, many=True)
        return Response(serializer.data)
    