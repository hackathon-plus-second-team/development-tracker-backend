"""Views for 'goals' endpoints of 'Api' application v1."""

from api.v1.drf_spectacular.custom_decorators import (
    activate_drf_spectacular_view_decorator,
)
from api.v1.goals.serializers import CreateUpdateGoalSerializer, ReadGoalSerializer
from api.v1.goals.viewsets import GetPostPatchDeleteViewSet
from goals.models import Goal


@activate_drf_spectacular_view_decorator
class GoalViewSet(GetPostPatchDeleteViewSet):
    """URL requests handler to 'Goals' resource endpoints."""

    name = "Goal resource"
    description = "API endpoints to manage goals."

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method in ("POST", "PATCH"):
            return CreateUpdateGoalSerializer
        return ReadGoalSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
