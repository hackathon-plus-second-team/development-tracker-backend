"""Fields for the endpoints 'tests' of the 'Api' application v1."""

from rest_framework import serializers

from level_tests.models import LevelTest, Question


class QuestionInTestField(serializers.SlugRelatedField):
    """SlugRelatedField for questions in selected test."""

    def get_queryset(self):
        level_test_id = self.context.get("level_test", None)
        queryset = Question.objects.filter(
            level_test=LevelTest.objects.get(id=level_test_id)
        )
        return queryset
