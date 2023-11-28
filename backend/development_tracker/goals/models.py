"""Database settings of the 'Goals' application."""

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.goals.field_limits import limits
from skills.models import Skill


class Goal(models.Model):
    """Model Goal."""

    name = models.CharField(
        "name",
        help_text="Skill's name",
        max_length=limits["GOAL_NAME_MAX_CHAR"],
        unique=True,
        error_messages={
            "unique": "A goal with this name already exists.",
        },
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="user",
        help_text="User",
        on_delete=models.PROTECT,
        related_name="goals",
    )
    skills = models.ManyToManyField(
        Skill,
        verbose_name="skills",
        help_text="Goals skills",
        related_name="goals",
    )
    level = models.PositiveSmallIntegerField(
        "level",
        help_text="Level",
        default=limits["GOAL_LEVEL_MIN_VALUE"],
        validators=(
            MinValueValidator(limits["GOAL_LEVEL_MIN_VALUE"]),
            MaxValueValidator(limits["GOAL_LEVEL_MAX_VALUE"]),
        ),
    )
    deadline = models.DateTimeField(
        "deadline",
        help_text="goal completion date",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "goal"
        verbose_name_plural = "goals"

    def __str__(self):
        return self.name
