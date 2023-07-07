from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializer import *
import random

# Create your views here.


@api_view(['GET'])
def getToDeliveries(request, id=None):
    if id is not None:
        try:
            
            delivery = DeliveryStatus.objects.get(id=id)
            serializer = Delivery_statusSerializer(delivery)  
            return Response(serializer.data)
        except DeliveryStatus.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        qs = DeliveryStatus.objects.all()
        serializer = Delivery_statusSerializer(qs, many=True)
        print(serializer.data)
        return Response(serializer.data)



@api_view(['POST'])
def createDelivery(request):
    serializer = Delivery_statusSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateDelivery(request, id):
    try:
        delivery = DeliveryStatus.objects.get(id=id)
        serializer = Delivery_statusSerializer(delivery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except DeliveryStatus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteDelivery(request, id):
    try:
        delivery = DeliveryStatus.objects.get(id=id)
        delivery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except DeliveryStatus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    



@api_view(['GET'])
def getPayments(request, id=None):
    if id is not None:
        try:
            
            payment = Payment.objects.get(id=id)
            serializer = PaymentSerializer(payment)  
            return Response(serializer.data)
        except Payment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        qs = Payment.objects.all()
        serializer = PaymentSerializer(qs, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def createPayment(request):
    serializer = PaymentSerializer(data=request.data)

    if serializer.is_valid():
        if serializer.validated_data['mode'] != "cod":
            tr = random.randint(1000000000000000, 9999999999999999)
            serializer.validated_data['transaction'] = tr
        else:
            serializer.validated_data['transaction'] = "COD"

        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def updatePayment(request, id):
    try:
        payment = Payment.objects.get(id=id)
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Payment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deletePayment(request, id):
    try:
        payment = Payment.objects.get(id=id)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Payment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def getCart(request, id=None):
    if id is not None:
        try:
            
            cart = Cart.objects.get(id=id)
            serializer = CartSerializer(cart)  
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        qs = Cart.objects.all()
        serializer = CartSerializer(qs, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def createCart(request):
    serializer = CartSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def updateCart(request, id):
    try:
        cart = Cart.objects.get(id=id)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteCart(request, id):
    try:
        cart = Cart.objects.get(id=id)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
