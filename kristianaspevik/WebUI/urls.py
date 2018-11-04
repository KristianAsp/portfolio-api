from django.urls import path, include
from . import views

urlpatterns = [
    path(r'', views.index),
    path(r'projects/', views.projects_index),
    path(r'about/', views.about_index)
]
