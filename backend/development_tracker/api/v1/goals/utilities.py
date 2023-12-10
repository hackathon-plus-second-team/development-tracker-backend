"""Helper functions for the endpoints 'goals' of 'Api' application v1."""

from django.contrib.auth import get_user_model

from api.v1.core.utilities import get_average_level, get_skills
from goals.models import Goal

User = get_user_model()


def update_goal_level(obj: Goal) -> None:
    """Update the goal level."""
    user = obj.user
    level = get_average_level(user, obj)
    obj.level = level
    obj.save()
