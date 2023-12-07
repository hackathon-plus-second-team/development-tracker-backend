"""Serializers for the endpoints 'tests' of 'Api' application v1."""

from django.db import transaction
from rest_framework import serializers

from api.v1.core.sample_recommendations import articles, courses
from api.v1.core.serializers import SkillProgressSerializer
from api.v1.level_tests.fields import QuestionInTestField
from core.level_tests.field_limits import FIELD_LIMITS_LEVEL_TESTS_APP
from level_tests.models import Answer, LevelTest, LevelTestProgress, Question
from skills.models import SkillProgress


class AnswerSerializer(serializers.ModelSerializer):
    """Serializer for work with level test answers to questions."""

    class Meta:
        model = Answer
        fields = ("name", "number")
        read_only_fields = fields


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer for work with level test questions."""

    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            "name",
            "explanation",
            "number",
            "answers",
        )
        read_only_fields = fields


class LevelTestSerializer(serializers.ModelSerializer):
    """Serializer for work with level test information."""

    skill = serializers.CharField(source="skill.name")
    questions = QuestionSerializer(many=True)

    class Meta:
        model = LevelTest
        fields = (
            "id",
            "name",
            "skill",
            "_get_count_questions",
            "questions",
        )
        read_only_fields = fields


class QuestionAnswerSerializer(serializers.Serializer):
    """Serializer to represent question and user's answer to the level test."""

    user_answer = serializers.IntegerField(write_only=True)
    question = QuestionInTestField(slug_field="number")

    default_error_messages = {
        "uncorrect_answer": "Question {question}: Selected answer is invalid.",
        "already_answered": "You have already answered this question",
    }

    def validate(self, data):
        question = data["question"]
        answer_min_value = FIELD_LIMITS_LEVEL_TESTS_APP["ANSWER_NUMBER_MIN_VALUE"]
        answer_max_value = question._get_count_answers()
        if not answer_min_value <= data["user_answer"] <= answer_max_value:
            raise serializers.ValidationError(
                self.error_messages["uncorrect_answer"].format(question=question.number)
            )
        return data

    def to_representation(self, instance):
        return super().to_representation(instance)


class LevelTestProgressReadSerializer(serializers.ModelSerializer):
    """Seriaizer to work with requests about level test results."""

    count_questions = serializers.IntegerField(source="level_test._get_count_questions")
    skill = serializers.CharField(source="level_test.skill")
    user = serializers.CharField(source="user.email")

    class Meta:
        model = LevelTestProgress
        fields = (
            "user",
            "skill",
            "level_test",
            "correct_answers",
            "count_questions",
            "percentage_correct",
        )
        read_only_fields = fields


class LevelTestUserAnswersSerializer(serializers.Serializer):
    """Serializer for working with user answers to the test."""

    user_answers = serializers.ListField(child=QuestionAnswerSerializer())

    default_error_messages = {
        "not_all_answers": "List does not contain answers to all the test questions",
        "not_unique_question": "List contains several answers to the same question",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level_test = None

    def validate_user_answers(self, value):
        self.level_test = LevelTest.objects.get(id=self.context.get("level_test"))

        if len(value) != self.level_test._get_count_questions():
            raise serializers.ValidationError(self.error_messages["not_all_answers"])

        answers_set = set()
        for answer in value:
            if answer["question"] in answers_set:
                raise serializers.ValidationError(
                    self.error_messages["not_unique_question"]
                )
            answers_set.add(answer["question"])

        return value

    @transaction.atomic
    def create(self, validated_data):
        correct_answers = 0
        for answer in validated_data["user_answers"]:
            answer["question"]._get_correct_answer()
            if answer["user_answer"] == answer["question"]._get_correct_answer().number:
                correct_answers += 1

        percentage_correct = (
            correct_answers / self.level_test._get_count_questions() * 100
        )

        request_user = self.context.get("request").user
        level_test_progress, _ = LevelTestProgress.objects.update_or_create(
            level_test=self.level_test,
            user=request_user,
            defaults={
                "correct_answers": correct_answers,
                "percentage_correct": percentage_correct,
            },
        )

        user_skill_progress, _ = SkillProgress.objects.get_or_create(
            user=request_user, skill=self.level_test.skill
        )
        if user_skill_progress.level <= percentage_correct:
            user_skill_progress.level = percentage_correct
            user_skill_progress.save(update_fields=("level",))

        return level_test_progress

    def to_representation(self, instance):
        return LevelTestProgressReadSerializer().to_representation(instance=instance)


class LevelTestResultWithRecommendationsSerializer(LevelTestProgressReadSerializer):
    """Serializer to work with requests about level test results.

    Add recommendations and skill progress info to response data.
    """

    def to_representation(self, instance):
        current_test = LevelTestProgressReadSerializer().to_representation(
            instance=instance
        )
        skill_progress = SkillProgressSerializer().to_representation(
            instance=SkillProgress.objects.get(
                user=instance.user, skill=instance.level_test.skill
            )
        )
        recommendations = {
            "courses": courses,
            "articles": articles,
        }
        return {
            "current_skill_test": current_test,
            "best_skill_result": skill_progress,
            "recommendations": recommendations,
        }
