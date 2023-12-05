"""Helper functions of 'Api' application v1."""

from django.contrib.auth import get_user_model

from api.v1.core.serializers import SkillProgressSerializer
from skills.models import Skill, SkillProgress

User = get_user_model()


def get_skills(user: User, obj: SkillProgress) -> list[Skill]:
    """Get list of skills for current user."""
    skills = obj.skills.all()
    skill_progresses = []

    for skill in skills:
        try:
            skill_progress = SkillProgress.objects.get(skill=skill, user=user)
        except SkillProgress.DoesNotExist:
            skill_progress = SkillProgress(skill=skill, user=user)

        skill_progresses.append(skill_progress)
    return SkillProgressSerializer(skill_progresses, many=True).data
