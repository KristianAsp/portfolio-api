from collections import OrderedDict

from rest_framework import serializers
from .models import Project, ProjectType, Tag


class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = OrderedDict(choices)
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        for i in self._choices:
            if self._choices[i] == obj:
                return self._choices[i]
        raise serializers.ValidationError("Acceptable values are {0}.".format(list(self._choices.values())))


    def to_internal_value(self, data):
        for i in self._choices:
            if self._choices[i] == data:
                return i
        raise serializers.ValidationError("Acceptable values are {0}.".format(list(self._choices.values())))


class ProjectSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(queryset = ProjectType.objects.all())
    class Meta:
        model = Project
        fields = ("title", "description", "type")


class ProjectTypeSerializer(serializers.ModelSerializer):
    title = ChoicesField(choices=ProjectType.PROJECT_TYPE_CHOICES)
    class Meta:
        model = ProjectType
        fields = ("title", )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name", )