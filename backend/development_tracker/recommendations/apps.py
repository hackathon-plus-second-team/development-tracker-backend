"""Configuration of 'recommendations' application."""

from django.apps import AppConfig


class RecommendationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "recommendations"
    verbose_name = "Recommendations management"