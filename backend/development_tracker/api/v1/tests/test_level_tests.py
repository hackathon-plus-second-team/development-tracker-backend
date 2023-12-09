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
            id=1, name="Django", skill=self.skill
        )
        self.question_1 = Question.objects.create(
            name="question 1",
            explanation="test question 1",
            number=1,
            level_test=self.level_test,
        )
        self.question_2 = Question.objects.create(
            name="question 2",
            explanation="test question 2",
            number=2,
            level_test=self.level_test,
        )
        self.question_3 = Question.objects.create(
            name="question 3",
            explanation="test question 3",
            number=3,
            level_test=self.level_test,
        )

        self.answer_1_question_1 = Answer.objects.create(
            name="answer_1_question_1",
            is_correct=True,
            number=1,
            question=self.question_1,
        )
        self.answer_2_question_1 = Answer.objects.create(
            name="answer_2_question_1",
            is_correct=False,
            number=2,
            question=self.question_1,
        )

        self.answer_1_question_2 = Answer.objects.create(
            name="answer_1_question_2",
            is_correct=True,
            number=1,
            question=self.question_2,
        )
        self.answer_2_question_2 = Answer.objects.create(
            name="answer_2_question_2",
            is_correct=False,
            number=2,
            question=self.question_2,
        )

        self.answer_1_question_3 = Answer.objects.create(
            name="answer_1_question_3",
            is_correct=True,
            number=1,
            question=self.question_3,
        )
        self.answer_2_question_3 = Answer.objects.create(
            name="answer_2_question_3",
            is_correct=False,
            number=2,
            question=self.question_3,
        )

    def test_level_test_detail(self):
        request = self.factory.get("/api/v1/tests/1/")
        force_authenticate(request, user=self.user)
        response = level_test_detail(request, 1)
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
            "/api/v1/tests/1/answer/", data=request_data, format="json"
        )
        force_authenticate(self.request, user=self.user)
        response = level_test_answer(self.request, 1)
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
            context={"request": self.request, "level_test": 1},
        )
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data, expected_data)

    def test_level_test_result(self):
        request = self.factory.get("/api/v1/tests/1/result/")
        force_authenticate(request, user=self.user)
        test_result = LevelTestProgress.objects.create(
            level_test=self.level_test,
            user=self.user,
            correct_answers=7,
            percentage_correct=8,
        )
        SkillProgress.objects.create(user=self.user, skill=self.skill)
        response = level_test_result(request, 1)
        data = response.data

        expected_data = LevelTestResultWithRecommendationsSerializer(
            test_result, context={"request": request}
        ).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, expected_data)
