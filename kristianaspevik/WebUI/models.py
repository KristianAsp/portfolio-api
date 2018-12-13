# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ProjectType(models.Model):
    PROJECT_TYPE_CHOICES = [
        ("Personal", "Personal"),
        ("University", "University"),
        ("Professional", "Professional"),
    ]
    title = models.CharField(max_length=30, choices=PROJECT_TYPE_CHOICES)


# Tags used to classify projects, i.e. "Open Source", "University"
class Tag(models.Model):
    name = models.CharField(max_length=20)


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    type = models.ForeignKey(to=ProjectType, on_delete=models.CASCADE)
