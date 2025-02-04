from django.urls import path
from myapi.views import IOCListCreate, IOCDetail

urlpatterns = [
    path('iocs/', IOCListCreate.as_view(), name='ioc-list'),
    path('iocs/<int:pk>/', IOCDetail.as_view, name='ioc-detail')
]
