from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
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
from admin_app.models import Admin
from django.http import JsonResponse

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
    log.info("user")
    log.info(user)
     
    admin=Admin.objects.filter(email=email).first()

    if user:
        log.info("Email exists**********************************************")
        log.error(password)
        log.error(user.password)
        if user.role=="ADMIN":
            if admin.status=="Active":
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
                return Response("status inactive")
               
        else:
         if user.role == 'CUSTOMER':   
            if check_password(password, user.password): # Verifying password
                log.info("Password is correct")
                # Generate JWT token
                log.info(user.id)
                user = Customer.objects.filter(email=email).first() 
                token = generate_jwt_token(user.id,user.email,user.role,user.first_name)
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
def generate_jwt_token(id,email,role,first_name):
    # Define the token payload (claims)
    payload = {
        'id' : id ,
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
        if otp:
            return Response(otp) #reponse as otp
        else:
            return Response('Something Went Wrong')
    else:
        log.info("Email is not exist")
        return Response("Email invalid") #reponse if email is not present



@api_view(['POST'])
def update_password(request):
    log.info("update_password:starts")
    email = request.data.get('email')
    password = request.data.get('password')
    log.info(password)
    user = Users.objects.get(email=email)
    log.info(user)
    role = user.role # Retrieve the user's role (assuming you have a 'role' field in the User model)
    log.info(role)
        # Perform any necessary operations based on the role
    if role == 'ADMIN':
        update=Admin.objects.filter(email=email).first() #get the user based on email
        update.set_password(password)
    
    else:
        update=Customer.objects.filter(email=email).first() #get the user based on email
        update.set_password(password) #password encodes
    log.info("Encoded password saved")
    h=update.save() #updtae the customer
    log.info(h)
    log.info("Password changed")
    return Response("Success") #reponse if password chnaged   


#for getting single user based on email
@api_view(['GET'])
def get_customer_by_EMail(request,email):
    log.info("get_customer_by_EMail start",email)
    #find the customer from db
    try:
        customer=Customer.objects.get(email=email)
        log.info("get_customer_by_EMail try block customer object",customer)
        serializers = CustomerSerializer(customer)
        data={
           'customer':serializers.data
        }
        log.info("get_customer_by_EMail try block json data",data)
        return JsonResponse(data)
    except Customer.DoesNotExist:
        raise Exception("Customer does not exist")
    except Exception:
        raise Exception("Something went wrong") 




