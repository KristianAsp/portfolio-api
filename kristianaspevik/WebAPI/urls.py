from django.urls import path
from .projects.views import ListCreateProjectsView, ProjectsDetailView, ListCreateProjectTypesView, ProjectTypesDetailView, ListCreateTagsView, TagDetailView

urlpatterns = [
    path('projects/', ListCreateProjectsView.as_view(), name="projects"),
    path('projects/<int:pk>/', ProjectsDetailView.as_view(), name="project-detail"),
    path('project-types/', ListCreateProjectTypesView.as_view(), name="project-types"),
    path('project-types/<int:pk>/', ProjectTypesDetailView.as_view(), name="project-type-detail"),
    path('tags/', ListCreateTagsView.as_view(), name="tags"),
    path('tags/<int:pk>/', TagDetailView.as_view(), name="tag-detail"),
]
