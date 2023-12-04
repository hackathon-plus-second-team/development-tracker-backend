"""URLs configuration of the 'Api' application v1."""

from django.urls import include, path

urlpatterns = [
    path("auth/", include("api.v1.auth.urls")),
    path("courses/", include("api.v1.courses.urls")),
    path("skills/", include("api.v1.skills.urls")),
    path("goals/", include("api.v1.goals.urls")),
]
