"""Serializers for the endpoints 'cources' of 'Api' application v1."""

from rest_framework import serializers

from api.v1.core.utilities import get_skills
from courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    """Serializer for viewing the user's paid courses."""

    skills = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "description",
            "skills",
        )

    def get_skills(self, obj):
        """Get a list of the course's skills."""
        return get_skills(self.context["request"].user, obj)


class CourseShortSerializer(CourseSerializer):
    """Serializer for short representation of course."""

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
        )
