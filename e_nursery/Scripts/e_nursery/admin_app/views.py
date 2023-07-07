

from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from customer_app.models import *
import logging as log
from rest_framework import status


#for the log level & file & formate
log.basicConfig(filename='e_nursery_log.log', level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


#for the log level & file & formate
log.basicConfig(filename='e_nursery_log.log', level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') 


@api_view(['POST'])
def registerAdmin(request):
    log.info("register_admin function started")
    try:  
            serilizer=AdminModelSerializer(data=request.data)  #serializer the admin data
            if serilizer.is_valid():  #checking the validation of serialized data
                log.info("register_admin:data is valid")
                email=request.data.get('email') #get email from request data
                log.info("Checking Email exits")
                data_exist=Users.objects.filter(email=email).exists() #check email is present or not
                if data_exist:
                    log.info("Email exist")
                    return Response("present") #email present then reponse
                else:
                    log.info("Email not exist")
                    serilizer.save()  #save the data into databse
                    log.info("Admin data is saved")
                    return Response(serilizer.data)  #return this response to frontend
            else:
                log.info("data is invalid")
                return Response("present")
    except Exception as e:
       return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 



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
    

@api_view(['PATCH'])
def update(request, id):
    try:
        admin = Admin.objects.get(id=id)
        log.info(admin)
        serializer = AdminModelSerializer(admin, data=request.data)
        log.info(serializer)
        admin.id=request.data.get('id')
        admin.first_name=request.data.get('first_name')
        admin.last_name=request.data.get('last_name')
        admin.email=request.data.get('email')
        try:                       
            admin.save()        # Save the updated Admin object
            serializer = AdminModelSerializer(admin)  # Return the serialized data in the response
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
          
    except Admin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
def status(request, id):
    log.info("Enter into insert admin")
    try:
        admin = Admin.objects.get(id=id)
    except Admin.DoesNotExist:
        return Response({'error': 'admin not found'}, status=status.HTTP_404_NOT_FOUND)

    # Assign the field value "InActive" to the desired field

    if (admin.status == "Active"):
        admin.status = "InActive"
    elif (admin.status == "InActive"):
        admin.status = "Active"
    else:
        admin.status = "Active"

                        
    try:                   # Save the updated Admin object
        admin.save()       # Return the serialized data in the response
        serializer = AdminModelSerializer(admin)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


