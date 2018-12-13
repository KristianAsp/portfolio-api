from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^projects/(?P<project_name>[A-Za-z0-9_])', views.project_detail, name="project_detail"),
    path(r'', views.index, name="home"),
    path(r'about', views.about_index, name="about"),
    path(r'contact', views.contact_index, name="contact"),
    path(r'projects', views.projects_index, name="projects"),
]
