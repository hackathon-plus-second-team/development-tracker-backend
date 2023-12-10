"""Tests for the endpoints 'skills' of 'Api' application v1."""

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate

from api.v1.skills.serializers import SkillForUserFullSerializer
from api.v1.skills.views import skill_user_detail
from skills.models import Skill, SkillProgress

User = get_user_model()


class SkillUserDetailTestCase(APITestCase):
    """Tests for user's skill detail."""

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            email="test@example.com", password="testpassword"
        )
        self.skill = Skill.objects.create(
            name="TypeScript", description="About TypeScript"
        )
        self.skill_progress = SkillProgress.objects.create(
            skill=self.skill, user=self.user
        )

    def test_skill_user_detail(self):
        request = self.factory.get(f"/api/v1/skills/{self.skill.id}/")
        force_authenticate(request, user=self.user)
        response = skill_user_detail(request, pk=self.skill.id)
        data = response.data
        expected_data = SkillForUserFullSerializer(
            self.skill_progress, context={"request": request}
        ).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, expected_data)
