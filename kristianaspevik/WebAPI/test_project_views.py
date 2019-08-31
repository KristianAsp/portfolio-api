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


