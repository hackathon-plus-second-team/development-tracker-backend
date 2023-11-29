"""Database settings of the 'Users' application."""

from django.contrib.auth.models import AbstractUser
from django.db import models

from core.users.field_limits import EMAIL_MAX_CHAR
from courses.models import Course
from users.managers import CustomUserManager


class User(AbstractUser):
    """Modified model User."""

    username = None
    email = models.EmailField(
        "email address",
        help_text="User's email address",
        max_length=EMAIL_MAX_CHAR,
        unique=True,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )
    paid_courses = models.ManyToManyField(
        Course,
        verbose_name="paid courses",
        help_text="User's paid courses",
        related_name="users",
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ()

    class Meta:
        ordering = ("email",)
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.email
