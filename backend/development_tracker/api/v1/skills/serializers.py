"""Serializers for the endpoints 'skills' of the 'Api' application v1."""

from rest_framework import serializers

from api.v1.core.serializers import SkillProgressSerializer
from api.v1.courses.serializers import CourseShortSerializer
from courses.models import Course
from skills.models import SkillProgress


class SkillForUserFullSerializer(SkillProgressSerializer):
    """Serializer for view full skill data for request user."""

    description = serializers.CharField(source="skill.description")
    level_test = serializers.PrimaryKeyRelatedField(
        source="skill.level_test.id",
        read_only=True,
    )

    class Meta:
        model = SkillProgress
        fields = (
            "id",
            "name",
            "description",
            "level",
            "level_test",
        )

    def to_representation(self, instance):
        user = self.context["request"].user
        ret = super().to_representation(instance)
        try:
            skill_user_cource = Course.objects.filter(skills=instance.skill, users=user)
            skill_user_cource_data = CourseShortSerializer(
                skill_user_cource, many=True, read_only=True
            ).data
        except Course.DoesNotExist:
            skill_user_cource_data = None

        ret.update({"user_cources": skill_user_cource_data})
        return ret
