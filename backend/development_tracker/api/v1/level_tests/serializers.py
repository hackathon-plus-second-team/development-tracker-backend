"""Serializers for the endpoints 'tests' of 'Api' application v1."""

from rest_framework import serializers

from level_tests.models import Answer, Choice, LevelTest, LevelTestProgress, Question
from core.level_tests.field_limits import FIELD_LIMITS_LEVEL_TESTS_APP


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


class ChoiceCreateSerializer(serializers.ModelSerializer):
    """Serializer to create user's Choice to level test questions."""

    answer_number = serializers.IntegerField(write_only=True)
    question = serializers.SlugRelatedField(slug_field="name", read_only=True)
    answer = serializers.SlugRelatedField(slug_field="name", read_only=True)

    default_error_messages = {
        "uncorrect_answer": "Selected answer is invalid.",
        "already_answered": "You have already answered this question",
    }

    class Meta:
        model = Choice
        fields = ("id", "user", "level_test", "question", "answer_number", "answer")
        read_only_fields = (
            "id",
            "user",
            "level_test",
        )

    def validate_answer_number(self, value):
        request_query_param = self.context["request"].parser_context["kwargs"]
        self.question = Question.objects.get(
            level_test=LevelTest.objects.get(id=request_query_param["test_id"]),
            number=request_query_param["question_number"],
        )
        answer_min_value = FIELD_LIMITS_LEVEL_TESTS_APP["ANSWER_NUMBER_MIN_VALUE"]
        answer_max_value = self.question._get_count_answers()

        if not answer_min_value <= value <= answer_max_value:
            raise serializers.ValidationError(self.error_messages["uncorrect_answer"])

        return value

    def validate(self, data):
        if Choice.objects.filter(
            user=self.context["request"].user,
            question=self.question,
            level_test=self.question.level_test,
        ).exists():
            raise serializers.ValidationError(self.error_messages["already_answered"])
        return data

    def create(self, validated_data):
        request_user = self.context["request"].user
        answer = Answer.objects.get(
            question=self.question, number=validated_data["answer_number"]
        )
        test = LevelTest.objects.get(
            id=self.context["request"].parser_context["kwargs"]["test_id"]
        )
        user_choice = Choice.objects.create(
            user=request_user, level_test=test, question=self.question, answer=answer
        )
        return user_choice

    def to_representation(self, instance):
        return super().to_representation(instance)

    # если уже существует выбор юзера на этот вопрос?
    # ПОСЛЕ РАСЧЕТА РЕЗУЛЬТАТА УДАЛЯТЬ ВСЕ ОТВЕТЫ ЮЗЕРА

    # обсудить с фронтами как они будут получат следубщий вопрос теста


class LevelTestProgressSerializer(serializers.ModelSerializer):
    """Seriaizer to work with requests about level test results."""

    count_answers = serializers.IntegerField(source="level_test._get_count_questions")

    class Meta:
        model = LevelTestProgress
        fields = (
            "user", "level_test", "choices", "correct_answers", "count_answers", "percentage_correct"
        )
        read_only_fields = fields
