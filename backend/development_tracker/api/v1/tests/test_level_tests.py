"""Tests for the endpoints 'tests' of 'Api' application v1."""

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate

from api.v1.level_tests.serializers import (
    LevelTestResultWithRecommendationsSerializer,
    LevelTestSerializer,
    LevelTestUserAnswersSerializer,
)
from api.v1.level_tests.views import (
    level_test_answer,
    level_test_detail,
    level_test_result,
)
from skills.models import Skill, SkillProgress
from level_tests.models import Answer, LevelTest, LevelTestProgress, Question

User = get_user_model()


class LevelTestDetailTestCase(APITestCase):
    """Tests for level tests."""

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.skill = Skill.objects.create(name="Django")
        self.user = User.objects.create_user(
            email="test@example.com", password="testpassword"
        )
        self.level_test = LevelTest.objects.create(
            name="Django", skill=self.skill
        )
        self.question_first = Question.objects.create(
            name="question first",
            explanation="test question first",
            number=1,
            level_test=self.level_test,
        )
        self.question_second = Question.objects.create(
            name="question second",
            explanation="test question second",
            number=2,
            level_test=self.level_test,
        )
        self.question_third = Question.objects.create(
            name="question third",
            explanation="test question third",
            number=3,
            level_test=self.level_test,
        )
        self.answer_first_question_first = Answer.objects.create(
            name="answer_first_question_first",
            is_correct=True,
            number=1,
            question=self.question_first,
        )
        self.answer_second_question_first = Answer.objects.create(
            name="answer_second_question_first",
            is_correct=False,
            number=2,
            question=self.question_first,
        )
        self.answer_first_question_second = Answer.objects.create(
            name="answer_first_question_second",
            is_correct=True,
            number=1,
            question=self.question_second,
        )
        self.answer_second_question_second = Answer.objects.create(
            name="answer_second_question_second",
            is_correct=False,
            number=2,
            question=self.question_second,
        )
        self.answer_first_question_third = Answer.objects.create(
            name="answer_first_question_third",
            is_correct=True,
            number=1,
            question=self.question_third,
        )
        self.answer_second_question_3 = Answer.objects.create(
            name="answer_second_question_3",
            is_correct=False,
            number=2,
            question=self.question_third,
        )

    def test_level_test_detail(self):
        request = self.factory.get(f"/api/v1/tests/{self.level_test.id}/")
        force_authenticate(request, user=self.user)
        response = level_test_detail(request, self.level_test.id)
        data = response.data

        expected_data = LevelTestSerializer(
            self.level_test, context={"request": request}
        ).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, expected_data)

    def test_level_test_answer(self):
        request_data = {
            "user_answers": [
                {"question": 1, "user_answer": 1},
                {"question": 2, "user_answer": 2},
                {"question": 3, "user_answer": 2},
            ]
        }
        self.request = self.factory.post(
            f"/api/v1/tests/{self.level_test.id}/answer/", data=request_data, format="json"
        )
        force_authenticate(self.request, user=self.user)
        response = level_test_answer(self.request, self.level_test.id)
        data = response.data

        level_test_progress, _ = LevelTestProgress.objects.update_or_create(
            level_test=self.level_test,
            user=self.user,
            defaults={
                "correct_answers": 1,
                "percentage_correct": 33,
            },
        )
        user_skill_progress, _ = SkillProgress.objects.get_or_create(
            user=self.user, skill=self.level_test.skill
        )
        if user_skill_progress.level <= 33:
            user_skill_progress.level = 33
            user_skill_progress.save(update_fields=("level",))

        serializer = LevelTestUserAnswersSerializer(
            instance=level_test_progress,
            context={"request": self.request, "level_test": self.level_test.id},
        )
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data, expected_data)

    def test_level_test_result(self):
        request = self.factory.get(f"/api/v1/tests/{self.level_test.id}/result/")
        force_authenticate(request, user=self.user)
        test_result = LevelTestProgress.objects.create(
            level_test=self.level_test,
            user=self.user,
            correct_answers=7,
            percentage_correct=8,
        )
        SkillProgress.objects.create(user=self.user, skill=self.skill)
        response = level_test_result(request, self.level_test.id)
        data = response.data

        expected_data = LevelTestResultWithRecommendationsSerializer(
            test_result, context={"request": request}
        ).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, expected_data)
