"""Admin site settings of the 'Goals' application."""

from django.contrib import admin

from goals.models import Goal


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    """Settings for presenting 'Goal' model on the admin site."""

    list_display = ("name", "user", "level", "deadline")
