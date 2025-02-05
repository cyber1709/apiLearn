from django.contrib import admin
from myapi.models import IOC, ProfileFeedItem
# Register your models here.


class ProfileFeedItemAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'status_text', 'created_on')
    search_fields = ('user_profile', 'status_text')
    
admin.site.register(ProfileFeedItem, ProfileFeedItemAdmin)


class IOCAdmin(admin.ModelAdmin):
    list_display = ('ip', 'domain', 'noticed_date', 'source')
    search_fields = ('ip', 'domain', 'noticed_date', 'source')
    
admin.site.register(IOC, IOCAdmin)