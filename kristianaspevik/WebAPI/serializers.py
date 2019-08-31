from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Project
        fields = ("title", "description", "type")
