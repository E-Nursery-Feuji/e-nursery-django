import logging as log
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *

#for the log level & file & formate
log.basicConfig(filename='e_nursery_log.log', level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create your views here.



#for save the cart with customer.product,quantity
@api_view(['POST'])
def createCart(request):
    
    log.info("createCart method start",request.data)
    log.info(request.data)
    serializer = CartSerializer(data=request.data)
    log.info("createCart ",serializer)

    if serializer.is_valid():
        log.info("data is valid",serializer)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    
    return Response(serializer.errors)
