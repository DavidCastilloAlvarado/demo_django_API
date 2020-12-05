from rest_framework import serializers
from apiapp.models import Customer


class Id_post_serializer(serializers.Serializer):
    id = serializers.IntegerField()


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
