"""Admin site settings of the 'Level_Tests' application."""

from django.contrib import admin

from level_tests.models import (
    Answer,
    Choice,
    LevelTest,
    LevelTestProgress,
    Question,
)


class AnswerInline(admin.TabularInline):
    """Settings for presenting 'Answer' model in 'Question' model."""

    model = Answer
    show_change_link = True


class QuestionInline(admin.TabularInline):
    """Settings for presenting 'Question' model in 'LevelTest' model."""

    model = Question
    show_change_link = True


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """Settings for presenting 'Answer' model on the admin site."""

    list_display = (
        "question",
        "number",
        "is_correct",
    )
    list_select_related = True
    fields = (
        "question",
        "number",
        "name",
        "is_correct",
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Settings for presenting 'Question' model on the admin site."""

    list_display = (
        "test",
        "number",
        "name",
        "_get_count_answers",
    )
    list_select_related = True
    fields = (
        "test",
        "number",
        "name",
        "explanation",
        "_get_count_answers",
    )
    readonly_fields = ("_get_count_answers",)
    inlines = (AnswerInline,)


@admin.register(LevelTest)
class LevelTestAdmin(admin.ModelAdmin):
    """Settings for presenting 'LevelTest' model on the admin site."""

    list_display = (
        "skill",
        "name",
        "_get_count_questions",
    )
    list_select_related = True
    fields = (
        "name",
        "skill",
        "_get_count_questions",
    )
    readonly_fields = ("_get_count_questions",)
    inlines = (QuestionInline,)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    """Settings for presenting 'Choice' model on the admin site."""

    list_display = (
        "user",
        "question",
        "answer",
    )
    fields = (
        "user",
        "question",
        "answer",
    )


@admin.register(LevelTestProgress)
class LevelTestProgressAdmin(admin.ModelAdmin):
    """Settings for presenting 'LevelTestProgress' model on the admin site."""

    list_display = (
        "user",
        "level_test",
        "percentage_correct",
    )
    fields = (
        "user",
        "level_test",
        "choices",
        "correct_answers",
        "percentage_correct",
    )
    readonly_fields = (
        "correct_answers",
        "percentage_correct",
    )
