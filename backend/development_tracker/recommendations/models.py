"""Database settings of the 'Recommendations' application."""

from django.conf import settings
from django.db import models

from articles.models import Article
from courses.models import Course


class Recommendation(models.Model):
    """Model Recommendation."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="user",
        help_text="User",
        on_delete=models.PROTECT,
        related_name="recommendations",
    )
    courses = models.ManyToManyField(
        Course,
        verbose_name="courses",
        help_text="Reccomendation's courses",
        related_name="recommendations",
    )
    articles = models.ManyToManyField(
        Article,
        verbose_name="articles",
        help_text="Reccomendation's articles",
        related_name="recommendations",
    )

    class Meta:
        verbose_name = "recommendation"
        verbose_name_plural = "recommendations"

    def __str__(self):
        return self.user.email
