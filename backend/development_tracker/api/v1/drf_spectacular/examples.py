"""Examples describing responses for use in documentation."""

from drf_spectacular.utils import OpenApiExample
from rest_framework import status

MyCoursesList200ResponseExample = OpenApiExample(
    name="MyCoursesList",
    description="Example to response 200 for user's paid courses list.",
    response_only=True,
    status_codes=[str(status.HTTP_200_OK)],
    value={
        "id": 0,
        "name": "string",
        "description": "string",
        "skills": [{"id": 0, "name": "string", "level": 0}],
        "level": 0
    },
)

SkillUserDetail200ResponseExample = OpenApiExample(
    name="SkillUserDetail",
    description="Example to response 200 for skill user detail.",
    response_only=True,
    status_codes=[str(status.HTTP_200_OK)],
    value={
        "id": 0,
        "name": "string",
        "description": "string",
        "level": 3,
        "level_test": 6,
        "user_cources": [{"id": 0, "name": "string"}],
    },
)

GoalUserDetail200ResponseExample = OpenApiExample(
    name="GoalUserDetail",
    description="Example to response 200 for goal user detail.",
    response_only=True,
    status_codes=[str(status.HTTP_200_OK)],
    value={
        "id": 0,
        "name": "string",
        "deadline": "2023-03-01T12:00:00Z",
        "skills": [{"id": 0, "name": "string", "level": 0}],
        "level": 23,
    },
)

LevelTestDetail200ResponseExample = OpenApiExample(
    name="LevelTestDetail",
    description="Example to response 200 for level test detail.",
    response_only=True,
    status_codes=[str(status.HTTP_200_OK)],
    value={
        "id": 0,
        "name": "string",
        "skill": "string",
        "_get_count_questions": 3,
        "questions": [
            {
                "name": 0,
                "explanation": "string",
                "number": 4,
                "answers": [{"name": "string", "number": 7}],
            }
        ],
    },
)

LevelTestUserAnswer201ResponseExample = OpenApiExample(
    name="LevelTestDetail",
    description="Example to response 200 for level test  user answer.",
    response_only=True,
    status_codes=[str(status.HTTP_201_CREATED)],
    value={
        "skill": "SQL",
        "level_test": 1,
        "correct_answers": 2,
        "count_questions": 3,
        "percentage_correct": 66,
    },
)

LevelTestResult200ResponseExample = OpenApiExample(
    name="LevelTestDetail",
    description="Example to response 200 for level test users result.",
    response_only=True,
    status_codes=[str(status.HTTP_200_OK)],
    value={
        "current_skill_test": {
            "skill": "string",
            "level_test": 1,
            "correct_answers": 2,
            "count_questions": 3,
            "percentage_correct": 66,
        },
        "best_skill_result": {"id": 1, "name": "string", "level": 100},
        "recommendations": {
            "courses": [
                {
                    "id": 3,
                    "name": "string",
                    "skills": "string",
                    "description": "string",
                    "url": "https://practicum.yandex.ru/frontend-developer/",
                },
            ],
            "articles": [
                {
                    "name": "string",
                    "url": "https://practicum.yandex.ru/blog/zachem-nuzhen-html/",
                }
            ],
        },
    },
)
