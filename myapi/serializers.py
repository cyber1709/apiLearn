from rest_framework import serializers
from myapi.models import IOC

class IOCSerializer(serializers.ModelSerializer):
    class Meta:
        model = IOC
        fields = '__all__'
        

class HelloSerializer(serializers.Serializer):
    """Serialiers serialises a name field for testing our api view"""
    name = serializers.CharField(max_length=10)
    