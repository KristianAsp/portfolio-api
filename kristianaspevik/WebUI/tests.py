# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Project, Tag, ProjectType

class ProjectTestCase(TestCase):
    def setUp(self):
        ProjectType.objects.create(title="Personal")
        type = ProjectType.objects.get(title="Personal")
        Project.objects.create(title="my test project", description="sample description", type=type).save()
        Project.objects.create(title="my test-project", description="sample description", type=type).save()
        Tag.objects.create(name="University")

    def test_set_project_link(self):
        """ Test Generated Project Links """
        project = Project.objects.get(title="my test project")
        self.assertEqual(project.link, 'my_test_project')
        project = Project.objects.get(title="my test-project")
        self.assertEqual(project.link, 'my_test-project')

    def test_add_project_tag(self):
        """ Test Adding Tag Post-Creation """
        project = Project.objects.get(title="my test project")

        project.tags.add(Tag.objects.get(name="University"))

        self.assertEqual(project.tags.count(), 1)

        project.tags.remove(Tag.objects.get(name="University"))

        self.assertEqual(project.tags.count(), 0)

    def test_removing_project_tag(self):
        """ Test Removing Tag Post-Creation """
        project = Project.objects.get(title="my test project")

        project.tags.add(Tag.objects.get(name="University"))

        self.assertEqual(project.tags.count(), 1)

        project.tags.remove(Tag.objects.get(name="University"))

        self.assertEqual(project.tags.count(), 0)
