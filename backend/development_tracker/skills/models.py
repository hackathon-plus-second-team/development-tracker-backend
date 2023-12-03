"""Database settings of the 'Skills' application."""

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.skills.field_limits import FIELD_LIMITS_SKILLS_APP


class Skill(models.Model):
    """Model Skill."""

    name = models.CharField(
        "name",
        help_text="Skill's name",
        max_length=FIELD_LIMITS_SKILLS_APP["SKILL_NAME_MAX_CHAR"],
        unique=True,
        error_messages={
            "unique": "A skill with this name already exists.",
        },
    )
    description = models.CharField(
        "description",
        help_text="Skill's description",
        max_length=FIELD_LIMITS_SKILLS_APP["SKILL_DESCRIPTION_MAX_CHAR"],
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
        verbose_name="skill",
        help_text="Skill",
        on_delete=models.PROTECT,
        related_name="skill_progresses",
    )
    level = models.PositiveSmallIntegerField(
        "level",
        help_text="Level",
        default=FIELD_LIMITS_SKILLS_APP["SKILL_LEVEL_MIN_VALUE"],
        validators=(
            MinValueValidator(FIELD_LIMITS_SKILLS_APP["SKILL_LEVEL_MIN_VALUE"]),
            MaxValueValidator(FIELD_LIMITS_SKILLS_APP["SKILL_LEVEL_MAX_VALUE"]),
        ),
    )

    class Meta:
        verbose_name = "skill progress"
        verbose_name_plural = "skill progresses"

    def __str__(self):
        return f"{self.skill.name} - {self.level}"
