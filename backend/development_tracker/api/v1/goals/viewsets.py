"""Viewsets for 'goals' endpoints of the 'Api' application v1."""

from rest_framework import viewsets


class GetPostPatchDeleteViewSet(viewsets.ModelViewSet):
    """The viewset allows methods: GET, POST, PATCH, DELETE."""

    http_method_names = ("get", "post", "patch", "delete", "head", "options")
