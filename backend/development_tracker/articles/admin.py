"""Admin site settings of the 'Articles' application."""

from django.contrib import admin

from articles.models import Article


class SkillInline(admin.TabularInline):
    """Settings for presenting 'Skill' model in 'Course' model."""

    model = Article.skills.through


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Settings for presenting 'Recommendation' model on the admin site."""

    list_display = (
        "name",
        "url",
    )
    inlines = (SkillInline,)
