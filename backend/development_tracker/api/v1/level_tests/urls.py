"""URLs configuration of the endpoints 'tests' of 'Api' application v1."""

from django.urls import path

from api.v1.level_tests.views import level_test_detail, level_test_question, level_test_result

urlpatterns = [
    path("<int:test_id>/", level_test_detail, name="level_test_detail"),
    path(
        "<int:test_id>/questions/<int:question_number>/",
        level_test_question,
        name="level_test_question",
    ),
    path("<int:test_id>/result/", level_test_result, name="level_test_result"),

]
