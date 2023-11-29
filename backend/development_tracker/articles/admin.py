"""Admin site settings of the 'Articles' application."""

from django.contrib import admin

from articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Settings for presenting 'Article' model on the admin site."""

    list_display = (
        "name",
        "url",
    )
