"""Database settings of the 'Skills' application."""

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.skills.field_limits import limits


class Skill(models.Model):
    """Model Skill."""

    name = models.CharField(
        "name",
        help_text="Skill's name",
        max_length=limits["SKILL_NAME_MAX_CHAR"],
        unique=True,
        error_messages={
            "unique": "A skill with this name already exists.",
        },
    )

    class Meta:
        verbose_name = "skill"
        verbose_name_plural = "skills"

    def __str__(self):
        return self.name


class SkillProgress(models.Model):
    """Model SkillProgress."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="user",
        help_text="User",
        on_delete=models.PROTECT,
        related_name="skill_progresses",
    )
    skill = models.ForeignKey(
        Skill,
        verbose_name="Skill",
        help_text="User",
        on_delete=models.PROTECT,
        related_name="skill_progresses",
    )
    level = models.PositiveSmallIntegerField(
        "level",
        help_text="Level",
        default=limits["SKILL_LEVEL_MIN_VALUE"],
        validators=(
            MinValueValidator(limits["SKILL_LEVEL_MIN_VALUE"]),
            MaxValueValidator(limits["SKILL_LEVEL_MAX_VALUE"]),
        ),
    )

    class Meta:
        verbose_name = "skill progress"
        verbose_name_plural = "skill progresses"

    def __str__(self):
        return f"{self.skill.name} - {self.level}"
