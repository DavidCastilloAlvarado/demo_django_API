from django.shortcuts import render

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apiapp import serializers
from apiapp.models import Customer
from django.http import JsonResponse
from django.core import serializers as serializers_core
import json


class Rest_api_customers(APIView):
    # api de prueba
    serializer_class = serializers.Id_post_serializer

    def get(self, request, format=None):
        """"
        Return all the customer allocated in our database
        """
        try:
            all_customers = Customer.objects.all()
            all_customers = serializers_core.serialize('json', all_customers, )
            all_customers = json.loads(all_customers)
            return Response([customer["fields"] for customer in all_customers])
        except:
            return Response(
                "Can't provide customers",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        """ Return the client information by ID"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            id = serializer.validated_data.get('id')
            try:
                customer = Customer.objects.get(id=id)
                customer = serializers_core.serialize('json', [customer], )
                return Response(json.loads(customer)[0]["fields"])
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
