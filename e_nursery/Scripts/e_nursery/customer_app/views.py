from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from .serializer import *
import logging as log
import jwt
from datetime import datetime, timedelta
from django.contrib.auth.hashers import check_password
from django.conf import settings
from .email import *

#for the log level & file & formate
log.basicConfig(filename='e_nursery_log.log', level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


#for registration of customer
@api_view(['POST'])
def register_customer(request):
    log.info("register_customer function started")
    serilizer=CustomerSerializer(data=request.data)  #serializer the customer data
    if serilizer.is_valid():  #checking the validation of serialized data
        log.info("register_customer:data is valid")
        email=request.data.get('email') #get email from request data
        log.info("Checking Email exits")
        data_exist=Users.objects.filter(email=email).exists() #check email is present or not
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
    

#for login the customer
@api_view(['POST'])
def login_customer(request):
    log.info("login_customer function started")
    serializer = LoginSerializer(data=request.data)
    email = request.data.get('email')
    password = request.data.get('password')
    user = Users.objects.filter(email=email).first() # Retrieve customer object based on email
    if user:
        log.info("Email exists**********************************************")
        log.error(password)
        log.error(user.password)
        if check_password(password, user.password): # Verifying password
            log.info("Password is correct")
            # Generate JWT token
            token = generate_jwt_token(user.email,user.role,user.first_name)
            # Include the token in the response
            response_data = {
                'user': UserSerializer(user).data,
                'token': token
            }
            return Response(response_data)
        else:
            log.info("Password is incorrect")
            return Response("Incorrect Password")
    else:
        log.info("Email does not exist")
        return Response("Email not found")
    
#for generating jwt token
def generate_jwt_token(email,role,first_name):
    # Define the token payload (claims)
    payload = {
        'email': email,
        'role':role,
        'first_name':first_name,
        'exp': datetime.utcnow() + timedelta(days=7)  # Set token expiration to 7 days from now
    }
    # Generate the JWT token using the secret key from Django settings
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token

# for forgotpassword
@api_view(['POST'])
def forgot_password(request):
    log.info("forgot_password:starts")
    email=request.data.get('email') #get email from request
    user = Users.objects.filter(email=email).first()
    if user:
        log.info("Email Exist")
        log.info("Email send function call")
        otp=send_opt_via_email(email) #send the otp method
        log.info("email send function return otp")
        log.info(otp)
        return Response(otp) #reponse as otp
    else:
        log.info("Email is not exist")
        return Response("Email invalid") #reponse if email is not present
    
@api_view(['POST'])
def update_password(request):
    log.info("update_password:starts")
    email=request.data.get('email') #get email from the request
    password=request.data.get('password') #get password form request
    customer=Customer.objects.filter(email=email).first() #get the user based on email
    customer.set_password(password) #password encodes
    log.info("Encoded password saved")
    h=customer.save() #updtae the customer
    log.info(h)
    log.info("Password changed")
    return Response("Success") #reponse if password chnaged
    


