import logging as log
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.core.exceptions import *

#for the log level & file & formate
log.basicConfig(filename='e_nursery_log.log', level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create your views here.



#for save the cart with customer.product,quantity
@api_view(['POST','PUT'])
def createCart(request):
    log.info("createCart method start")
    log.info(request.data)
    try:
        if request.method == 'POST':
            log.info("Call post method")
            serializer = CartSerializer(data=request.data)
        elif request.method == 'PUT':
            log.info("Call Put method")
            cart_id = request.data.get('id')
            cart_instance = Cart.objects.get(id=cart_id)
            serializer=CartSerializer(cart_instance,data=request.data)
        log.info("Data serialized")
        if serializer.is_valid():
            log.info("data is valid")
            serializer.save()
            log.info("Data saved")
            return Response(serializer.data)
        else:
            log.info("Data is not valid")
            return Response(serializer.errors)
    except Exception as e:
        log.error("Enter in except block")
        raise Exception("Something went wrong in createCart method")

#get cart by the customer id
@api_view(['GET'])
def cart(request, id):
    log.info("cart method start")
    try:
        log.info("cart method:if method start")
        cart_queryset = Cart.objects.filter(customer_id=id)
        cart = cart_queryset.first()
        if cart is None:
            raise ObjectDoesNotExist("No object found in cart with this id")
        
        log.info(cart.id)
        cart_list = [model_to_dict(cart) for cart in cart_queryset]
        log.info("dict")
        log.info(cart_list)
        data = {
            'cart': cart_list
        }
        return JsonResponse(data)
    except ObjectDoesNotExist as e:
        log.error(str(e))
        error_message = "There is no object in the cart with this id"
        data = {
            'error': error_message
        }
        return JsonResponse(data, status=404)  # Return 404 status code for not found
    except Exception as e:
        log.info("cart method: enter the except block")
        log.error(str(e))
        error_message = "Something went wrong in the cart method"
        data = {
            'error': error_message
        }
        return JsonResponse(data, status=500)  # Return 500 status code for internal server error


