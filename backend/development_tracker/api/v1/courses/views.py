"""Views for 'courses' endpoints of 'Api' application v1."""

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from api.v1.drf_spectacular.custom_decorators import (
    activate_drf_spectacular_view_decorator,
)
from api.v1.courses.serializers import CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@activate_drf_spectacular_view_decorator
@api_view(("GET",))
def my_courses(request):
    """List of courses paid for by the user."""
    paid_courses = request.user.paid_courses.all()
    serializer = CourseSerializer(paid_courses, many=True, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)
