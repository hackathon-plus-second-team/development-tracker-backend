"""Database settings of the 'Courses' application."""

from django.db import models

from core.courses.field_limits import limits
from skills.models import Skill


class Course(models.Model):
    """Model Course."""

    name = models.CharField(
        "name",
        help_text="Course's name",
        max_length=limits["COURSE_NAME_MAX_CHAR"],
        unique=True,
        error_messages={
            "unique": "A course with this name already exists.",
        },
    )
    description = models.CharField(
        "description",
        help_text="Course's description",
        max_length=limits["DESCRIPTION_MAX_CHAR"],
        unique=True,
        error_messages={
            "unique": "A course with this description already exists.",
        },
    )
    skills = models.ManyToManyField(
        Skill,
        verbose_name="skills",
        help_text="Course's skills",
        related_name="courses",
    )

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"

    def __str__(self):
        return self.name
