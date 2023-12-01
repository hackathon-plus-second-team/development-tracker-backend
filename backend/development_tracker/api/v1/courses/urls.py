"""URLs configuration of the endpoints 'courses' of 'Api' application v1."""

from django.urls import path

from api.v1.courses.views import my_courses

urlpatterns = [
    path("my_courses/", my_courses, name="my_courses"),
]
