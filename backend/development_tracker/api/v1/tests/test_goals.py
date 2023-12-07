"""Tests for the endpoints 'goals' of 'Api' application v1."""

import datetime
import json

import pytz
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate

from api.v1.goals.serializers import ReadGoalSerializer
from api.v1.goals.views import GoalViewSet
from goals.models import Goal
from skills.models import Skill

User = get_user_model()


class GoalViewSetTestCase(APITestCase):
    """Tests for GoalViewSet."""

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(
            email="test@example.com", password="testpassword"
        )
        self.goal = Goal.objects.create(
            name="My Goal",
            deadline=pytz.utc.localize(datetime.datetime(2023, 3, 1, 13, 0, 0)),
            user=self.user,
        )
        self.skill_first = Skill.objects.create(name="Python")
        self.skill_second = Skill.objects.create(name="Django")
        self.goal.skills.add(self.skill_first, self.skill_second)
        self.skill_third = Skill.objects.create(name="SQL")

    def test_get_goals_list(self):
        request = self.factory.get("/api/v1/goals/")
        force_authenticate(request, user=self.user)
        view = GoalViewSet.as_view({"get": "list"})
        response = view(request)
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 1)

    def test_get_goal_detail(self):
        request = self.factory.get(f"/api/v1/goals/{self.goal.id}/")
        force_authenticate(request, user=self.user)
        view = GoalViewSet.as_view({"get": "retrieve"})
        response = view(request, pk=self.goal.id)
        data = response.data

        serializer = ReadGoalSerializer(
            instance=self.goal, context={"request": request}
        )
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, expected_data)

    def test_create_goal(self):
        request_data = {
            "name": "My_goal",
            "deadline": "2023-03-01T13:00:00",
            "skills": [self.skill_first.id, self.skill_second.id],
        }
        self.request = self.factory.post("/api/v1/goals/", data=request_data)
        force_authenticate(self.request, user=self.user)
        view = GoalViewSet.as_view({"post": "create"})
        response = view(self.request)
        data = response.data

        goal_id = response.data["id"]
        goal = Goal.objects.get(id=goal_id)

        serializer = ReadGoalSerializer(
            instance=goal, context={"request": self.request}
        )
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data, expected_data)

    def test_update_goal(self):
        request_data = {
            "name": "Updated Goal",
            "deadline": "2023-03-15T18:00:00",
            "skills": [self.skill_third.id],
        }
        goal_id = self.goal.id
        url = f"/api/v1/goals/{goal_id}/"
        self.request = self.factory.patch(
            url, data=json.dumps(request_data), content_type="application/json"
        )
        force_authenticate(self.request, user=self.user)
        view = GoalViewSet.as_view({"patch": "partial_update"})
        response = view(self.request, pk=goal_id)
        data = response.data

        goal = Goal.objects.get(id=goal_id)
        serializer = ReadGoalSerializer(
            instance=goal, context={"request": self.request}
        )
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, expected_data)

    def test_delete_goal(self):
        goal_id = self.goal.id
        url = f"/api/v1/goals/{goal_id}/"
        self.request = self.factory.delete(url)
        force_authenticate(self.request, user=self.user)
        view = GoalViewSet.as_view({"delete": "destroy"})
        response = view(self.request, pk=goal_id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Goal.objects.filter(id=goal_id).exists())
