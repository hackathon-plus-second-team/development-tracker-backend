"""URLs configuration of the endpoints 'courses' of the 'Api' application v1."""

from django.urls import path

from api.v1.courses.views import my_courses

urlpatterns = [
    path("my/", my_courses, name="my_courses"),
]
