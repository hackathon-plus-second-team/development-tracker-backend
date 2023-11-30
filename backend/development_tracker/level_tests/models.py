"""Database settings of the 'Level_Tests' application."""

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.level_tests.field_limits import FIELD_LIMITS_LEVEL_TESTS_APP
from skills.models import Skill


class LevelTest(models.Model):
    """Model LevelTest."""

    name = models.CharField(
        "level test name",
        help_text="Name of the level test",
        max_length=FIELD_LIMITS_LEVEL_TESTS_APP["LEVEL_TEST_NAME_MAX_CHAR"],
        unique=True,
        error_messages={
            "unique": "A level test with this name already exists.",
        },
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.SET_NULL,
        verbose_name="skill",
        help_text="Skill for test",
        related_name="level_test",
        null=True,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "level test"
        verbose_name_plural = "level tests"

    def __str__(self):
        return self.name

    def _get_count_questions(self):
        """Get count of questions in level test."""
        return self.questions.count()

    _get_count_questions.short_description = "count of questions in level test"


class Question(models.Model):
    """Model Question."""

    name = models.CharField(
        "question text",
        help_text="Text of the question",
        max_length=FIELD_LIMITS_LEVEL_TESTS_APP["QUESTION_NAME_MAX_CHAR"],
    )
    explanation = models.CharField(
        "question explanation",
        help_text="Text of the question explanation",
        max_length=FIELD_LIMITS_LEVEL_TESTS_APP["QUESTION_EXPLANATION_MAX_CHAR"],
        blank=True,
    )
    number = models.PositiveSmallIntegerField(
        "question number in test",
        help_text="Number of this question in the test",
        validators=(
            MinValueValidator(
                FIELD_LIMITS_LEVEL_TESTS_APP["QUESTION_NUMBER_MIN_VALUE"]
            ),
            MaxValueValidator(
                FIELD_LIMITS_LEVEL_TESTS_APP["QUESTION_NUMBER_MAX_VALUE"]
            ),
        ),
    )
    test = models.ForeignKey(
        LevelTest,
        on_delete=models.CASCADE,
        verbose_name="test",
        help_text="Test",
        related_name="questions",
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "question"
        verbose_name_plural = "questions"

    def __str__(self):
        return f"question {self.number} to level test {self.test}"

    def _get_count_answers(self):
        """Get count of questions in level test."""
        return self.answers.count()

    _get_count_answers.short_description = "count of answers to question"


class Answer(models.Model):
    """Model Answer."""

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name="question",
        help_text="Question",
        related_name="answers",
    )
    name = models.CharField(
        "answer text",
        help_text="Answer to the question",
        max_length=FIELD_LIMITS_LEVEL_TESTS_APP["ANSWER_NAME_MAX_CHAR"],
    )
    is_correct = models.BooleanField(
        "is answer correct",
        help_text="Indicates the answer is correct",
        default=False,
    )
    number = models.PositiveSmallIntegerField(
        "answer number for order in test questions",
        help_text="Number of this answer in the test questions",
        validators=(
            MinValueValidator(FIELD_LIMITS_LEVEL_TESTS_APP["ANSWER_NUMBER_MIN_VALUE"]),
            MaxValueValidator(FIELD_LIMITS_LEVEL_TESTS_APP["ANSWER_NUMBER_MAX_VALUE"]),
        ),
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "answer"
        verbose_name_plural = "answers"

    def __str__(self):
        return f"answer {self.id} to question {self.question}"


class Choice(models.Model):
    """Model Choice. Represent users choice."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="user",
        help_text="User",
        related_name="choices",
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name="question",
        help_text="Question",
        related_name="choices",
    )
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        verbose_name="answer",
        help_text="Answer",
        related_name="choices",
    )

    class Meta:
        ordering = ("user",)
        verbose_name = "choice"
        verbose_name_plural = "choices"

    def __str__(self):
        return f"{self.question} - {self.answer} by {self.user}"


class LevelTestProgress(models.Model):
    """Model LevelTestProgress."""

    level_test = models.ForeignKey(
        LevelTest,
        on_delete=models.PROTECT,
        verbose_name="level test",
        help_text="Level test",
        related_name="level_test_progress",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="user",
        help_text="User",
        related_name="level_test_progress",
    )
    choices = models.ManyToManyField(
        Choice,
        verbose_name="choices",
        help_text="Choices",
        related_name="level_test_progress",
    )
    correct_answers = models.PositiveSmallIntegerField(
        "count of correct answers in level test",
        help_text="Count of correct answers in level test",
        default=FIELD_LIMITS_LEVEL_TESTS_APP["LEVEL_TEST_PROGRESS_MIN_ANSWERS"],
        validators=(
            MinValueValidator(
                FIELD_LIMITS_LEVEL_TESTS_APP["LEVEL_TEST_PROGRESS_MIN_ANSWERS"]
            ),
            MaxValueValidator(
                FIELD_LIMITS_LEVEL_TESTS_APP["LEVEL_TEST_PROGRESS_MAX_ANSWERS"]
            ),
        ),
    )
    wrong_answers = models.PositiveSmallIntegerField(
        "count of wrong answers in level test",
        help_text="Count of wrong answers in level test",
        default=FIELD_LIMITS_LEVEL_TESTS_APP["LEVEL_TEST_PROGRESS_MIN_ANSWERS"],
        validators=(
            MinValueValidator(
                FIELD_LIMITS_LEVEL_TESTS_APP["LEVEL_TEST_PROGRESS_MIN_ANSWERS"]
            ),
            MaxValueValidator(
                FIELD_LIMITS_LEVEL_TESTS_APP["LEVEL_TEST_PROGRESS_MAX_ANSWERS"]
            ),
        ),
    )
    percentage_correct = models.DecimalField(
        "percentage of correct answers",
        help_text="percentage of correct answers",
        max_digits=4,
        decimal_places=2,
        default=0,
    )

    class Meta:
        ordering = ("user",)
        verbose_name = "level test progress"
        verbose_name_plural = "level test progresses"

    def __str__(self) -> str:
        return f"""{self.level_test} for {self.user} result is
            {self.percentage_correct} %."""
