"""URL configuration of the 'development_tracker' application."""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/", include("api.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("admin/", admin.site.urls),
    ]
