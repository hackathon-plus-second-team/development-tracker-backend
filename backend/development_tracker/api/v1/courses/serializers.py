"""Serializers for the endpoints 'auth' of 'Api' application v1."""

from rest_framework import serializers

from courses.models import Course
from skills.models import Skill, SkillProgress


class SkillProgressSerializer(serializers.ModelSerializer):
    """Serializer for viewing skill progresses."""

    id = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(), source="skill.id"
    )
    name = serializers.CharField(source="skill.name")

    class Meta:
        model = SkillProgress
        fields = (
            "id",
            "name",
            "level",
        )


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
