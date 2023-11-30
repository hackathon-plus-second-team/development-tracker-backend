"""URLs configuration of the 'api' application."""

from django.conf import settings
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

app_name = "api"

urlpatterns = [path("v1/", include("api.v1.urls"))]

if settings.DEBUG:
    urlpatterns += (
        path(
            "dynamic_doc/download/v1/",
            SpectacularAPIView.as_view(),
            name="schema",
        ),
        path(
            "dynamic_doc/swagger/v1/",
            SpectacularSwaggerView.as_view(url_name="api:schema"),
            name="swagger",
        ),
    )
