"""Views for 'tests' endpoints of the Api' application v1."""

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.v1.drf_spectacular.custom_decorators import (
    activate_drf_spectacular_view_decorator,
)
from api.v1.level_tests.serializers import (
    LevelTestResultWithRecommendationsSerializer,
    LevelTestSerializer,
    LevelTestUserAnswersSerializer,
)
from level_tests.models import LevelTest, LevelTestProgress


@activate_drf_spectacular_view_decorator
@api_view()
def level_test_detail(request, test_id):
    """Process requests about level test with id=test_id."""
    test = get_object_or_404(LevelTest, id=test_id)
    serializer = LevelTestSerializer(test, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@activate_drf_spectacular_view_decorator
@api_view(("POST",))
def level_test_answer(request, test_id):
    """Process requests about write user answers to level test."""
    serializer = LevelTestUserAnswersSerializer(
        data=request.data, context={"request": request, "level_test": test_id}
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@activate_drf_spectacular_view_decorator
@api_view()
def level_test_result(request, test_id):
    """Process requests about results of level test with id=test_id."""
    test = get_object_or_404(LevelTest, id=test_id)
    test_result = LevelTestProgress.objects.get(level_test=test, user=request.user)
    serializer = LevelTestResultWithRecommendationsSerializer(
        test_result, context={"request": request}
    )
    return Response(serializer.data, status=status.HTTP_200_OK)
