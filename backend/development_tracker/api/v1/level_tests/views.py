"""Views for 'tests' endpoints of 'Api' application v1."""

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.v1.level_tests.serializers import (
    ChoiceCreateSerializer,
    LevelTestProgressSerializer,
    LevelTestSerializer,
    QuestionSerializer,
)
from level_tests.models import LevelTest, LevelTestProgress, Question


@api_view()
# дсотуп - тем, у кого есть навык теста
def level_test_detail(request, test_id):
    """Process requests about level test with id=test_id."""
    test = get_object_or_404(LevelTest, id=test_id)
    serializer = LevelTestSerializer(test, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(("GET", "POST"))
# дсотуп - тем, у кого есть навык теста и кто не прошел еще этот тест
def level_test_question(request, test_id, question_number):
    """Process requests about level test with test_id questions with question_number."""
    test = get_object_or_404(LevelTest, id=test_id)
    question = get_object_or_404(
        Question.objects.filter(level_test=test), number=question_number
    )

    if request.method == "GET":
        serializer = QuestionSerializer(question, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    serializer = ChoiceCreateSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view()
def level_test_result(request, test_id):
    """Process requests about results of level test with id=test_id."""
    test = get_object_or_404(LevelTest, id=test_id)
    test_result = LevelTestProgress(level_test=test, user=request.user)
    serializer = LevelTestProgressSerializer(test_result, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)
