from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
import logging as log
from rest_framework import status


#for the log level & file & formate
log.basicConfig(filename='e_nursery_log.log', level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Create your views here.

@api_view(['POST'])
def register_customer(request):
    log.info("register_customer function started")
    serilizer=AdminModelSerializer(data=request.data)  #serializer the customer data
    if serilizer.is_valid():  #checking the validation of serialized data
        log.info("register_customer:data is valid")
        email=request.data.get('email') #get email from request data
        log.info("Checking Email exits")
        data_exist=Admin.objects.filter(email=email).exists() #check email is present or not
        if data_exist:
            log.info("Email exist")
            return Response("present") #email present then reponse
        else:
            log.info("Email not exist")
            serilizer.save()  #save the data into databse
            log.info("customer data is saved")
            return Response(serilizer.data)  #return this response to frontend
    else:
        log.info("data is invalid")
        return Response("present")
    
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