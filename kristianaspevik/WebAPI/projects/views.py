from __future__ import unicode_literals
from ..models import Project, ProjectType, Tag
from ..serializers import ProjectSerializer, ProjectTypeSerializer, TagSerializer
from rest_framework import generics, serializers
from rest_framework.response import Response
from rest_framework.views import status
from .decorators import validate_project_request_data, validate_project_type_request_data, validate_tag_request_data

class ListCreateProjectsView(generics.ListCreateAPIView):
    """
    GET projects/
    POST projects/
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def post(self, request, *args, **kwargs):
        project = ProjectSerializer(data = request.data)
        if project.is_valid():
            project.save()

            return Response(
                data=project.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
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
            serializer = ProjectSerializer(project, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Project.DoesNotExist:
            return Response(
                data={
                    "message": "Project with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ListCreateProjectTypesView(generics.ListCreateAPIView):
    """
        GET project-types/
        POST project-types/
        """

    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer

    def post(self, request, *args, **kwargs):
        try:
            project_type = ProjectTypeSerializer(data = request.data)
            if project_type.is_valid():
                project_type.save()

                return Response(
                    data=project_type.data,
                    status=status.HTTP_201_CREATED
                )
            else:
                raise serializers.ValidationError
        except serializers.ValidationError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ProjectTypesDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET projects/:id/
    PUT projects/:id/
    DELETE projects/:id/
    """
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer

    def get(self, request, *args, **kwargs):
        try:
            project_type = self.queryset.get(pk=kwargs["pk"])
            return Response(ProjectTypeSerializer(project_type).data)
        except Project.DoesNotExist:
            return Response(
                data = {
                    "message": "ProjectType with id: {} does not exist".format(kwargs["pk"])
                },
                status = status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            project_type = self.queryset.get(pk=kwargs["pk"])
            project_type.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProjectType.DoesNotExist:
            return Response(
                data={
                    "message": "ProjectType with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_project_type_request_data
    def put(self, request, *args, **kwargs):
        try:
            project_type = self.queryset.get(pk=kwargs["pk"])
            serializer = ProjectTypeSerializer(project_type, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

            return Response(status = status.HTTP_400_BAD_REQUEST)
        except ProjectType.DoesNotExist:
            return Response(
                data={
                    "message": "ProjectType with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ListCreateTagsView(generics.ListCreateAPIView):
    """
    GET tags/
    POST tags/
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def post(self, request, *args, **kwargs):
        tag = TagSerializer(data = request.data)
        if tag.is_valid():
            tag.save()

            return Response(
                data=tag.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                status = status.HTTP_400_BAD_REQUEST
            )

class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET tags/:id/
    PUT tags/:id/
    DELETE tags/:id/
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        try:
            tag = self.queryset.get(pk=kwargs["pk"])
            return Response(TagSerializer(tag).data)
        except Tag.DoesNotExist:
            return Response(
                data = {
                    "message": "Tag with id: {} does not exist".format(kwargs["pk"])
                },
                status = status.HTTP_404_NOT_FOUND
            )


    @validate_tag_request_data
    def put(self, request, *args, **kwargs):
        try:
            tag = self.queryset.get(pk=kwargs["pk"])
            serializer = TagSerializer(tag, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(
                    status = status.HTTP_400_BAD_REQUEST
                )
        except Tag.DoesNotExist:
            return Response(
                data={
                    "message": "Tag with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


    def delete(self, request, *args, **kwargs):
        try:
            tag = self.queryset.get(pk=kwargs["pk"])
            tag.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tag.DoesNotExist:
            return Response(
                data = {
                    "message": "Tag with id: {} does not exist".format(kwargs["pk"])
                },
                status = status.HTTP_404_NOT_FOUND
            )