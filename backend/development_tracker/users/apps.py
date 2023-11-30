"""Configuration of 'Users' application."""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Settings of 'users' application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
    verbose_name = "Users management"
