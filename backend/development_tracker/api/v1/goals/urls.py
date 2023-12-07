"""URLs configuration of the endpoints 'goals' of 'Api' application v1."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.goals.views import GoalViewSet

router_v1 = DefaultRouter()

router_v1.register("", GoalViewSet, basename="goals")

urlpatterns = [path("", include(router_v1.urls))]
