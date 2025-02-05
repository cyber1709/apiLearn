from  myapi.serializers import UserProfileSerializer
from rest_framework import viewsets
from users.models import UserProfile
from rest_framework.authentication import TokenAuthentication
from myapi.permisions import UpdateOwnProfile

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles""" 
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)

