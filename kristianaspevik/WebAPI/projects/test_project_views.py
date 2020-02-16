from __future__ import unicode_literals

import json

from django.urls import reverse
from ..models import Project, Tag, ProjectType
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from ..serializers import ProjectSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_project(title="", description="", type=None):
        if title != "" and description != "" and type is not None:
            Project.objects.create(title=title,description=description,type=type).save()

    def setUp(self):
        ProjectType.objects.create(title="Personal")
        type = ProjectType.objects.get(title="Personal")
        self.create_project(title="my test project", description="sample description", type=type)
        self.create_project(title="my test-project2", description="sample description", type=type)
        Tag.objects.create(name="University")

        self.valid_data = {
            "title": "test project",
            "description": "test description",
            "type": 1,
            "tags": []
        }

        self.invalid_data = {
            "title": "test project",
            "type": 1
        }


class GetProjectsTest(BaseViewTest):
    def test_get_all_projects(self):
        """
        This test ensures that all projects added in the
        setup method exists when we make a GET request to the
        projects/ endpoint
        """

        response = self.client.get(
            reverse("projects", kwargs={"version": "v1"})
        )
        expected = Project.objects.all()
        serialized = ProjectSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_single_project(self):
        response = self.client.get(
            reverse("project-detail", kwargs={"version": "v1", "pk":1})
        )

        expected = Project.objects.get(id=1)
        serialized = ProjectSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteProjectsTest(BaseViewTest):
    def test_delete_single_project(self):
        response = self.client.delete(
            reverse("project-detail", kwargs={"version": "v1", "pk":1})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_non_existing_project(self):
        response = self.client.delete(
            reverse("project-detail", kwargs={"version": "v1", "pk": 100})
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateProjectsTest(BaseViewTest):
    def test_update_single_project(self):
        response = self.client.put(
            reverse("project-detail", kwargs={"version": "v1", "pk":1}), data=json.dumps(self.valid_data), content_type='application/json'
        )
        expected = Project.objects.get(id=1)
        serialized = ProjectSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_single_project_bad_data(self):
        response = self.client.put(
            reverse("project-detail", kwargs={"version": "v1", "pk": 1}), data=json.dumps(self.invalid_data), content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CreateProjectsTest(BaseViewTest):
    def test_create_new_project(self):
        response = self.client.post(
            reverse("projects", kwargs={"version": "v1"}), data=json.dumps(self.valid_data),
            content_type="application/json"
        )

        self.assertEqual(response.data, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
