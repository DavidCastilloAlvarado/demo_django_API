from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apiapp import serializers
from apiapp.models import Customer
from drf_yasg.utils import swagger_auto_schema
import json


# class Many_Customers(ReadOnlyModelViewSet):
#     """"
#     Return all the customer allocated in our database (2 way)
#     """
#     serializer_class = serializers.CustomerSerializer
#     queryset = Customer.objects.all()

class Customer_API(APIView):
    # api de prueba
    serializer_income = serializers.Id_post_serializer
    serializer_class = serializers.CustomerSerializer

    @swagger_auto_schema(
        responses={200: serializer_class(many=True)},
        tags=['List of Customers'],
    )
    def get(self, request, format=None):
        """"Return the whole list of customer allocated in our database """
        queryset = Customer.objects.all()
        queryset = self.serializer_class(queryset, many=True)
        return Response(queryset.data)

    @swagger_auto_schema(request_body=serializer_income, responses={200: serializer_class}, tags=['One Customer'])
    def post(self, request, format=None):
        """ Return the client information by ID"""
        serializer = self.serializer_income(data=request.data)
        if serializer.is_valid():
            id = serializer.validated_data.get('id')
            try:
                customer = Customer.objects.get(id=id)
                customer = self.serializer_class(customer)
                return Response(customer.data)
            except:
                return Response(
                    "Error query",
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
