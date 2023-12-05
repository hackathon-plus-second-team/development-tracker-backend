"""Helper functions for the endpoints 'goals' of 'Api' application v1."""

from django.contrib.auth import get_user_model

from api.v1.core.utilities import get_skills
from goals.models import Goal

User = get_user_model()


def get_goal_level(user: User, obj: Goal) -> int:
    """Calculate the goal level."""

    skill_progresses = get_skills(user, obj)
    level_sum = 0
    count = 0

    for skill_progress in skill_progresses:
        level_sum += skill_progress["level"]
        count += 1

    avg_level = level_sum / count if count > 0 else 0
    return int(avg_level)


def update_goal_level(obj: Goal) -> None:
    """Update the goal level."""
    user = obj.user
    level = get_goal_level(user, obj)
    obj.level = level
    obj.save()
