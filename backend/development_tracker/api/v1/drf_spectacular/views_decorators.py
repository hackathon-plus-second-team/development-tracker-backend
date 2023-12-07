"""Views decorators for use in documentation."""

from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from rest_framework import status

from api.v1.auth.serializers import AuthUserSignInSerilizer
from api.v1.courses.serializers import CourseSerializer
from api.v1.drf_spectacular.examples import (
    GoalUserDetail200ResponseExample,
    LevelTestDetail200ResponseExample,
    LevelTestResult200ResponseExample,
    LevelTestUserAnswer201ResponseExample,
    MyCoursesList200ResponseExample,
    SkillUserDetail200ResponseExample,
)
from api.v1.drf_spectacular.serializers import (
    Response200TokensSerializer,
    Response400Serializer,
    Response401Serializer,
    Response404Serializer,
)
from api.v1.goals.serializers import CreateUpdateGoalSerializer, ReadGoalSerializer
from api.v1.level_tests.serializers import (
    LevelTestResultWithRecommendationsSerializer,
    LevelTestSerializer,
    LevelTestUserAnswersSerializer,
)
from api.v1.skills.serializers import SkillForUserFullSerializer

VIEWS_DECORATORS = {
    "signin": extend_schema(
        tags=("auth",),
        request=AuthUserSignInSerilizer,
        responses={
            status.HTTP_200_OK: Response200TokensSerializer,
            status.HTTP_400_BAD_REQUEST: Response400Serializer,
            status.HTTP_404_NOT_FOUND: Response404Serializer,
        },
    ),
    "my_courses": extend_schema(
        tags=("courses",),
        responses={
            status.HTTP_200_OK: CourseSerializer,
            status.HTTP_401_UNAUTHORIZED: Response401Serializer,
        },
        examples=[
            MyCoursesList200ResponseExample,
        ],
    ),
    "skill_user_detail": extend_schema(
        tags=("skills",),
        responses={
            status.HTTP_200_OK: SkillForUserFullSerializer,
            status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            status.HTTP_404_NOT_FOUND: Response404Serializer,
        },
        examples=[
            SkillUserDetail200ResponseExample,
        ],
    ),
    "level_test_detail": extend_schema(
        tags=("tests",),
        responses={
            status.HTTP_200_OK: LevelTestSerializer,
            status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            status.HTTP_404_NOT_FOUND: Response404Serializer,
        },
        examples=[
            LevelTestDetail200ResponseExample,
        ],
    ),
    "level_test_answer": extend_schema(
        tags=("tests",),
        responses={
            status.HTTP_201_CREATED: LevelTestUserAnswersSerializer,
            status.HTTP_400_BAD_REQUEST: Response400Serializer,
            status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            status.HTTP_404_NOT_FOUND: Response404Serializer,
        },
        examples=[
            LevelTestUserAnswer201ResponseExample,
        ],
    ),
    "level_test_result": extend_schema(
        tags=("tests",),
        responses={
            status.HTTP_200_OK: LevelTestResultWithRecommendationsSerializer,
            status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            status.HTTP_404_NOT_FOUND: Response404Serializer,
        },
        examples=[
            LevelTestResult200ResponseExample,
        ],
    ),
    "GoalViewSet": extend_schema_view(
        create=extend_schema(
            tags=("goals",),
            responses={
                status.HTTP_201_CREATED: CreateUpdateGoalSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
        list=extend_schema(
            tags=("goals",),
            responses={
                status.HTTP_200_OK: ReadGoalSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
            examples=[
                GoalUserDetail200ResponseExample,
            ],
        ),
        retrieve=extend_schema(
            tags=("goals",),
            responses={
                status.HTTP_200_OK: ReadGoalSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_403_FORBIDDEN: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
            examples=[
                GoalUserDetail200ResponseExample,
            ],
        ),
        partial_update=extend_schema(
            tags=("goals",),
            responses={
                status.HTTP_200_OK: CreateUpdateGoalSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
            examples=[
                GoalUserDetail200ResponseExample,
            ],
        ),
        destroy=extend_schema(
            tags=("goals",),
            responses={
                status.HTTP_204_NO_CONTENT: OpenApiResponse(response=None),
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
    ),
}
