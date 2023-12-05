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
