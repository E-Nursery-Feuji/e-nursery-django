from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging as log
from customer_app.models import Users

#for the log level & file & formate
log.basicConfig(filename='e_nursery_log.log', level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') 


# for save the admin
@api_view(['POST'])
def saveAdmin(request):
    log.info("saveAdmin function is started")
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
        return Response(serializer.errors) #if data is not valid then send errors
