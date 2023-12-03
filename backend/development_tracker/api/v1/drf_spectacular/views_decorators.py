"""Views decorators for use in documentation."""

from drf_spectacular.utils import extend_schema
from rest_framework import status

from api.v1.auth.serializers import AuthUserSignInSerilizer
from api.v1.drf_spectacular.serializers import (
    Response200TokensSerializer,
    Response400Serializer,
    Response401Serializer,
    Response404Serializer,
)
from api.v1.drf_spectacular.examples import (
    MyCoursesList200ResponseExample,
    SkillUserDetail200ResponseExample,
)
from api.v1.courses.serializers import CourseSerializer
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
}
