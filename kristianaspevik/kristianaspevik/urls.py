from django.urls import path, include

urlpatterns = [
    path(r'', include('WebAPI.urls')),
    path(r'admin', include('administrator.urls')),
]
