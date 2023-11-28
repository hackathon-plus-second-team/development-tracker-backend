"""Database settings of the 'Articles' application."""

from django.db import models

from core.articles.field_limits import limits
from skills.models import Skill


class Article(models.Model):
    """Model Article."""

    name = models.CharField(
        "name",
        help_text="Article's name",
        max_length=limits["ARTICLE_NAME_MAX_CHAR"],
        unique=True,
        error_messages={
            "unique": "An article with this name already exists.",
        },
    )
    url = models.URLField(
        "url",
        help_text="Article's url",
        max_length=limits["ARTICLE_URL_MAX_CHAR"],
        unique=True,
        error_messages={
            "unique": "An article with this url already exists.",
        },
    )
    skills = models.ManyToManyField(
        Skill,
        verbose_name="skills",
        help_text="Article's skills",
        related_name="articles",
    )

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"

    def __str__(self):
        return self.name
