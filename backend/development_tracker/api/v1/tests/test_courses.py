"""Tests for the endpoints 'courses' of 'Api' application v1."""

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate

from api.v1.courses.serializers import CourseSerializer
from api.v1.courses.views import my_courses
from skills.models import Skill
from courses.models import Course

User = get_user_model()


class MyCoursesTestCase(APITestCase):
    """Tests for my courses."""

    def setUp(self):
        self.factory = APIRequestFactory()
        self.course = Course.objects.create(
            name="Python Developer", description="About Python"
        )
        self.skill_first = Skill.objects.create(name="TypeScript")
        self.skill_second = Skill.objects.create(name="HTML")
        self.course.skills.add(self.skill_first, self.skill_second)
        self.user = User.objects.create_user(
            email="test@example.com", password="testpassword"
        )
        self.user.paid_courses.add(self.course)

    def test_my_courses(self):
        request = self.factory.get("/api/v1/courses/my/")
        force_authenticate(request, user=self.user)
        response = my_courses(request)
        data = response.data
        expected_data = CourseSerializer(
            [self.course], many=True, context={"request": request}
        ).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, expected_data)
