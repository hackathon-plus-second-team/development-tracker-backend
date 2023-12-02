"""Admin site settings of the 'Courses' application."""

from django.contrib import admin

from courses.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Settings for presenting 'Course' model on the admin site."""

    list_display = ("id", "name", "description")
    search_fields = ("name",)
