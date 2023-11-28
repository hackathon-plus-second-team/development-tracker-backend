"""Admin site settings of the 'Recommendations' application."""

from django.contrib import admin

from recommendations.models import Recommendation


class CourseInline(admin.TabularInline):
    """Settings for presenting 'Course' model in 'Recommendation' model."""

    model = Recommendation.courses.through


class ArticleInline(admin.TabularInline):
    """Settings for presenting 'Article' model in 'Recommendation' model."""

    model = Recommendation.articles.through


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    """Settings for presenting 'Recommendation' model on the admin site."""

    list_display = ("user",)
    inlines = (
        CourseInline,
        ArticleInline,
    )
