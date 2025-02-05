from django.db import models
from django.conf import settings


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return the model as a string"""
        return self.status_text
    
    
# Create your models here.
class IOC(models.Model):
    ip = models.CharField(max_length=50, null=True)
    domain = models.CharField(max_length=100, null=True)
    noticed_date = models.DateTimeField(max_length=50, null=True)
    source = models.CharField(max_length=50, null=True)



    