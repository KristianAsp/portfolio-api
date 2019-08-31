from django.urls import path
from .views import ListCreateProjectsView, ProjectsDetailView

urlpatterns = [
    path('projects/', ListCreateProjectsView.as_view(), name="projects"),
    path('projects/<int:pk>/', ProjectsDetailView.as_view(), name="project-detail")
]
