"""URLs configuration of the endpoints 'skills' of 'Api' application v1."""

from django.urls import path

from api.v1.skills.views import skill_user_detail

urlpatterns = [
    path("<int:pk>/", skill_user_detail, name="skill_detail"),
]
