"""Views for 'courses' endpoints of the 'Api' application v1."""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.v1.drf_spectacular.custom_decorators import (
    activate_drf_spectacular_view_decorator,
)
from api.v1.courses.serializers import CourseSerializer


@activate_drf_spectacular_view_decorator
@api_view()
def my_courses(request):
    """List of courses paid for by the user."""
    paid_courses = request.user.paid_courses.all()
    serializer = CourseSerializer(paid_courses, many=True, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)
