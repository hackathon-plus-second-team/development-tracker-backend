"""Configuration of 'Skills' application."""

from django.apps import AppConfig


class SkillsConfig(AppConfig):
    """Settings of 'skills' application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "skills"
    verbose_name = "Skills management"
