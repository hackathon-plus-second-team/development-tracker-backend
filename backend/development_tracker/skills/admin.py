"""Admin site settings of the 'Skills' application."""

from django.contrib import admin

from skills.models import Skill, SkillProgress


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Settings for presenting 'Skill' model on the admin site."""

    list_display = ("name",)
    search_fields = ("name",)


@admin.register(SkillProgress)
class SkillProgressAdmin(admin.ModelAdmin):
    """Settings for presenting 'SkillProgress' model on the admin site."""

    list_display = (
        "user",
        "skill",
        "level",
    )
