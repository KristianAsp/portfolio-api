from __future__ import unicode_literals

import json

from django.urls import reverse
from ..models import Tag
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from ..serializers import TagSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_tag(name=""):
        if name != "":
            Tag.objects.create(name=name).save()

    def setUp(self):
        self.create_tag(name="Web Development")
        self.create_tag(name="Django")

        self.valid_data = {
            "name": "Test Tag"
        }

class GetTagsTest(BaseViewTest):
    def test_get_all_tags(self):
        response = self.client.get(
            reverse("tags", kwargs={"version": "v1"})
        )
        tags = Tag.objects.all()
        expected = TagSerializer(tags, many = True)
        self.assertEqual(response.data, expected.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_tag(self):
        response = self.client.get(
            reverse("tag-detail", kwargs={"version": "v1", "pk":1})
        )

        tag = Tag.objects.get(id = 1)
        expected = TagSerializer(tag)
        self.assertEqual(response.data, expected.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateTagsTest(BaseViewTest):
    def test_create_new_tag(self):
        response = self.client.post(
            reverse("tags", kwargs={"version": "v1"}), data=json.dumps(self.valid_data), content_type="application/json"
        )

        self.assertEqual(response.data, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateTagsTest(BaseViewTest):
    def test_update_existing_tag(self):
        response = self.client.put(
            reverse("tag-detail", kwargs={"version": "v1", "pk": 1}), data=json.dumps(self.valid_data), content_type="application/json"
        )

        tag = Tag.objects.get(id = 1)
        expected = TagSerializer(tag)
        self.assertEqual(response.data, expected.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
