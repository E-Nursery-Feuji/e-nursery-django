from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework import generics
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging as log

#for the log level & file & formate
log.basicConfig(filename='e_nursery_log.log', level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') 


# created by Priya Patel & Samundar Singh & Haritha 
# Create your views here.

# for save the customer
@api_view(['POST'])
def saveCustomer(request):
    log.info("saveCustomer funation is started")
    serializer=CustomerModelSerializer(data=request.data) #serialize the data
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

# for login user & admin
@api_view(['POST'])
def login(request):
    log.info("login function started")
    serializer=LoginSerializer(data=request.data)
    if serializer.is_valid():
        log.info("Data is Valid")
        email=request.data.get('email') #get email from request data
        password = request.data.get('password') # Get password from request data
        log.info("Checking Email if exits")
        user = Users.objects.filter(email=email).first() # Retrieve customer object based on email
        if user: #checking the customer is present
            log.info("Email exist")
            if password==user.password: #checking password
                log.info("Password is correct")
                userJson=UserSerializer(user) #convert to json
                return Response(userJson.data) #response if password is correct
            else:
                log.info("Password is incorrect")
                return Response("Incorrect Password") #reponse if password incorrect
        else:
            log.info("Email does not exist")
            return Response("Email not found") #email not present then reponse
    else:
        log.info("Invalid data") #data is nvalid
        return Response(serializer.errors) #reponse the errors