from django.shortcuts import render
from rest_framework import generics
from myapi.serializers import IOCSerializer, HelloSerializer
from myapi import serializers
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
from rest_framework import status

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    
    
    def get(self, request, format=None):
        """Returns a list of ApiView features"""
        an_apiview = [
            'uses http methods as functions (get, post, put, delete)',
            'is similar to a traditional django view',
            'gives you the most control over the application logic',
            'is mapped manually to URLs',
        ]
        
        return Response({'message' : 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request, pk=None):
        """Handles updating an object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """Handles partial update of an object"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})