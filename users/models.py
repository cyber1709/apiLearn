from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password=None):
        """Create and return a superuser"""
        user = self.create_user(
            email=email,
            name=name,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database model for users in the system.
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Can access admin site
    date_joined = models.DateTimeField(auto_now_add=True)
    
    objects = UserProfileManager()  # Custom manager for user profiles
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']  # Fields required when creating a superuser
    
    # Add related_name to avoid reverse accessor conflict
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='userprofile_set',  # Custom related_name to avoid clash
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='userprofile_set',  # Custom related_name to avoid clash
        blank=True
    )
    
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    
    def __str__(self):
        """Return string representation of user"""
        return self.email
