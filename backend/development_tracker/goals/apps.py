"""Configuration of the 'Goals' application."""

from django.apps import AppConfig


class GoalsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "goals"
    verbose_name = "Goals management"
