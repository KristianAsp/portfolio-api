from django.urls import path, include

urlpatterns = [
    path(r'', include('WebUI.urls')),
    path(r'admin', include('administrator.urls')),
]
