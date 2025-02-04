from django.contrib import admin
from users.models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_superuser', 'is_staff', 'last_login')

admin.site.register(UserProfile, UserProfileAdmin)