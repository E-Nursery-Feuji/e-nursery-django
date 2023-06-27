from django.shortcuts import render
from django.http import HttpResponse as Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
# Create your views here.
from rest_framework import status

def demo(request):
    return HttpResponse('orders app')

@api_view(['GET'])
def getAllPaymentstatus(request):
        try:
            payments = Payment.objects.all()
            serializer = PaymentSerializer(payments,many=True)  
            return Response(serializer.data)
        except Payment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def savePayment(request):
        try:
           
            serializer = PaymentSerializer(data=request.data)  
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Payment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)





# @api_view(['PUT'])
# def updateTotalUnits(request, total_units_id):
#     try:
#         patient = TotalUnits.objects.get(total_units_id=total_units_id)
#         serializer = TotalUnitsSerializer(patient, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except TotalUnits.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


# @api_view(['DELETE'])
# def deleteTotalUnits(request, total_units_id):
#     try:
#         total_units = TotalUnits.objects.get(total_units_id=total_units_id)
#         total_units.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     except TotalUnits.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)