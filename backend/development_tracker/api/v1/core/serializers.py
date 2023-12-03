"""Serializers for the 'Api' application v1."""

from rest_framework import serializers

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
