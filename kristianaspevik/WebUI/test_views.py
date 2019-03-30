# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Project, Tag, ProjectType

# See https://stackoverflow.com/questions/11885211/how-to-write-a-unit-test-for-a-django-view for 
# examples on how to test views
class ProjectViewsTestCase(TestCase):
    def setUp(self):
        ProjectType.objects.create(title="Personal")
        type = ProjectType.objects.get(title="Personal")
        Project.objects.create(title="my test project", description="sample description", type=type).save()
        Project.objects.create(title="my test-project", description="sample description", type=type).save()
        Tag.objects.create(name="University")

    def test_about_index_response_code(self):
        """ Test About Index """
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_about_index_template(self):
        response = self.client.get('/about')
        self.assertTemplateUsed(response, 'UI/index.html')

    def test_contact_index_response_code(self):
        """ Test About Index """
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_contact_index_template(self):
        response = self.client.get('/contact')
        self.assertTemplateUsed(response, 'UI/contact/index.html')

    def test_projects_index_response_code(self):
        """ Test About Index """
        response = self.client.get('/projects')
        self.assertEqual(response.status_code, 200)

    def test_projects_index_template(self):
        response = self.client.get('/projects')
        self.assertTemplateUsed(response, 'UI/projects/index.html')

    def test_project_detail_index_response_code(self):
        response = self.client.get('/projects')
        self.assertEqual(response.status_code, 200)

    def test_project_detail_index_template(self):
        response = self.client.get('/projects/my_test_project')
        self.assertTemplateUsed(response, 'UI/projects/detail.html')
