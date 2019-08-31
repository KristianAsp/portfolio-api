from __future__ import unicode_literals
from .models import Project, ProjectType
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from .serializers import ProjectSerializer
from .decorators import validate_project_request_data

class ListCreateProjectsView(generics.ListCreateAPIView):
    """
    GET projects/
    POST projects/
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def post(self, request, *args, **kwargs):
        project = Project.objects.create(
            title = request.data["title"],
            description = request.data["description"]
        )

        return Response(
            data=ProjectSerializer(project).data,
            status=status.HTTP_201_CREATED
        )


class ProjectsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET projects/:id/
    PUT projects/:id/
    DELETE projects/:id/
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):
        try:
            project = self.queryset.get(pk=kwargs["pk"])
            return Response(ProjectSerializer(project).data)
        except Project.DoesNotExist:
            return Response(
                data = {
                    "message": "Project with id: {} does not exist".format(kwargs["pk"])
                },
                status = status.HTTP_404_NOT_FOUND
            )


    def delete(self, request, *args, **kwargs):
        try:
            project = self.queryset.get(pk=kwargs["pk"])
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            return Response(
                data={
                    "message": "Project with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_project_request_data
    def put(self, request, *args, **kwargs):
        try:
            project = self.queryset.get(pk=kwargs["pk"])
            serializer = ProjectSerializer()
            request.data["type"] = ProjectType.objects.get(id = request.data["type"])
            updated_project = serializer.update(project, request.data)
            return Response(ProjectSerializer(updated_project).data)
        except Project.DoesNotExist:
            return Response(
                data={
                    "message": "Project with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )