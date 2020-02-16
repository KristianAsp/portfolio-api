from django.urls import path, include, re_path

urlpatterns = [
    re_path('api/(?P<version>(v1|v2))/', include('WebAPI.urls'))
]
