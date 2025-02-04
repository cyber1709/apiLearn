from django.contrib import admin
from myapi.models import IOC
# Register your models here.

class IOCAdmin(admin.ModelAdmin):
    list_display = ('ip', 'domain', 'noticed_date', 'source')
    search_fields = ('ip', 'domain', 'noticed_date', 'source')
    
admin.site.register(IOC, IOCAdmin)