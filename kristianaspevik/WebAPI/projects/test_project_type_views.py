# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.urls import reverse
from ..models import ProjectType
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from ..serializers import ProjectTypeSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_project(title=""):
        if title != "":
            ProjectType.objects.create(title=title).save()

    def setUp(self):
        ProjectType.objects.create(title="Personal")
        ProjectType.objects.create(title="Professional")
        ProjectType.objects.create(title="University")

        self.valid_data = {
            "title": "University",
        }

        self.invalid_data = {
            "title": "Test invalid value"
        }


class GetProjectTypesTest(BaseViewTest):
    def test_get_all_project_types(self):
        """
        This test ensures that all project types added in the
        setup method exists when we make a GET request to the
        projects/ endpoint
        """

        response = self.client.get(
            reverse("project-types", kwargs={"version": "v1"})
        )
        expected = ProjectType.objects.all()
        serialized = ProjectTypeSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_single_project_type(self):
        response = self.client.get(
            reverse("project-type-detail", kwargs={"version": "v1", "pk":1})
        )

        expected = ProjectType.objects.get(id=1)
        serialized = ProjectTypeSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateProjectTypesTest(BaseViewTest):
    def test_create_project_type(self):
        response = self.client.post(
            reverse("project-types", kwargs={"version": "v1"}), data=json.dumps(self.valid_data), content_type="application/json"
        )

        self.assertEqual(response.data, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_project_type_invalid_data(self):
        response = self.client.post(
            reverse("project-types", kwargs={"version": "v1"}), data=json.dumps(self.invalid_data), content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteProjectTypesTest(BaseViewTest):
    def test_delete_single_project_type(self):
        response = self.client.delete(
            reverse("project-type-detail", kwargs={"version": "v1", "pk": 1})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_non_existing_project_type(self):
        response = self.client.delete(
            reverse("project-type-detail", kwargs={"version": "v1", "pk": 99999})
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateProjectTypesTest(BaseViewTest):
    def test_update_non_existing_project_type(self):
        response = self.client.put(
            reverse("project-type-detail", kwargs={"version": "v1", "pk": 99999}), data=json.dumps(self.valid_data),
            content_type="application/json"
        )
        expected = {"message": "ProjectType with id: {} does not exist".format("99999")}
        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_update_existing_project_type(self):
        response = self.client.put(
            reverse("project-type-detail", kwargs={"version": "v1", "pk": 1}), data=json.dumps(self.valid_data),
            content_type="application/json"
        )
        expected = ProjectType.objects.get(id=1)
        serialized = ProjectTypeSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)