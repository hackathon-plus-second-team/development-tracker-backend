"""Views for 'skills' endpoints of 'Api' application v1."""

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.v1.drf_spectacular.custom_decorators import (
    activate_drf_spectacular_view_decorator,
)
from api.v1.skills.serializers import SkillForUserFullSerializer
from skills.models import Skill, SkillProgress


@activate_drf_spectacular_view_decorator
@api_view()
def skill_user_detail(request, pk):
    """Get skill data for request user."""
    skill = get_object_or_404(Skill, id=pk)
    skill_progress = get_object_or_404(SkillProgress, skill=skill, user=request.user)
    serializer = SkillForUserFullSerializer(
        skill_progress, context={"request": request}
    )
    return Response(serializer.data, status=status.HTTP_200_OK)
