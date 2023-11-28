"""Module provides application administration functionality."""

from django.contrib import admin


class DevelopmentTrackerAdminSite(admin.AdminSite):
    """Custom admin site."""

    site_header = "Development Tracker. Admin Site."
    site_title = "Development Tracker."
