"""Serializers for the endpoints 'cources' of 'Api' application v1."""

from rest_framework import serializers

from api.v1.core.serializers import SkillProgressSerializer
from courses.models import Course
from skills.models import Skill, SkillProgress


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

    def get_skills(self, obj: SkillProgress) -> list[Skill]:
        """Get list of skills for current course."""
        request_user = self.context["request"].user
        skills = obj.skills.all()
        skill_progresses = []

        for skill in skills:
            try:
                skill_progress = SkillProgress.objects.get(
                    skill=skill, user=request_user
                )
            except SkillProgress.DoesNotExist:
                skill_progress = SkillProgress(skill=skill, user=request_user)

            skill_progresses.append(skill_progress)
        return SkillProgressSerializer(skill_progresses, many=True).data


class CourseShortSerializer(CourseSerializer):
    """Serializer for short representation of course."""

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
        )
