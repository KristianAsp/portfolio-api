from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name="home"),
    path(r'projects', views.projects_index, name="projects"),
    path(r'about', views.about_index, name="about"),
    path(r'contact', views.contact_index, name="contact")
]
