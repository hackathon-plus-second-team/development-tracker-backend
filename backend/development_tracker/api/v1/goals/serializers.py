"""Serializers for the endpoints 'goals' of the 'Api' application v1."""

from rest_framework import serializers

from api.v1.core.utilities import get_average_level, get_skills
from api.v1.goals.utilities import update_goal_level
from goals.models import Goal
from skills.models import Skill


class ReadGoalSerializer(serializers.ModelSerializer):
    """Serializer for reading goals."""

    skills = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()

    class Meta:
        model = Goal
        fields = (
            "id",
            "name",
            "deadline",
            "skills",
            "level",
        )

    def get_skills(self, obj):
        """Get a list of the goal's skills."""
        return get_skills(self.context["request"].user, obj)

    def get_level(self, obj):
        """Get the goal level."""
        return get_average_level(self.context["request"].user, obj)


class CreateUpdateGoalSerializer(serializers.ModelSerializer):
    """Serializer for creating goals."""

    skills = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(),
        many=True,
        required=True,
    )

    class Meta:
        model = Goal
        fields = (
            "name",
            "deadline",
            "skills",
        )

    def create(self, validated_data):
        skills = validated_data.pop("skills")
        goal = super().create(validated_data)
        goal.skills.set(skills)
        update_goal_level(goal)
        return goal

    def update(self, instance, validated_data):
        skills = validated_data.get("skills")
        if skills is not None:
            for skill in skills:
                instance.skills.add(skill)

            existing_skills = instance.skills.all()
            for skill in existing_skills:
                if skill not in skills:
                    instance.skills.remove(skill)

        super().update(instance, validated_data)
        instance.save()
        update_goal_level(instance)
        return instance

    def to_representation(self, instance):
        return ReadGoalSerializer(instance, context=self.context).data
