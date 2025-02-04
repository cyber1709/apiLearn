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
    


from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    
    def get(self, request, format=None):
        """Returns a list of ApiView features"""
        an_apiview = [
            'uses http methods as functions (get, post, put, delete)',
            'is similar to a traditional django view',
            'gives you the most control over the application logic',
            'is mapped manually to URLs',
        ]
        
        return Response({'message' : 'Hello!', 'an_apiview': an_apiview})