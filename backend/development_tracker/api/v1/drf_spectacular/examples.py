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
