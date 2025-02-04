from django.shortcuts import render
from rest_framework import generics
from myapi.serializers import IOCSerializer
from myapi.models import IOC
# Create your views here.

class IOCListCreate(generics.ListCreateAPIView):
    queryset = IOC.objects.all()
    serializer_class = IOCSerializer
    
class IOCDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IOC.objects.all()
    serializer_class= IOCSerializer
    