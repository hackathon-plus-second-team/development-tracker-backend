"""Admin site settings of the 'Courses' application."""

from django.contrib import admin

from courses.models import Course


class SkillInline(admin.TabularInline):
    """Settings for presenting 'Skill' model in 'Course' model."""

    model = Course.skills.through


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Settings for presenting 'Course' model on the admin site."""

    list_display = ("name", "description")
    search_fields = ("name",)
    inlines = (SkillInline,)
