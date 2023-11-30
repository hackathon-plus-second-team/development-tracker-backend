"""Views for 'auth' endpoints of 'Api' application v1."""

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api.v1.auth.serializers import AuthUserSignInSerilizer

User = get_user_model()


@api_view(("POST",))
@permission_classes((AllowAny,))
def signin(request):
    """Authenticate user and issue JWT-tokens."""
    serializer = AuthUserSignInSerilizer(data=request.data)
    serializer.is_valid(raise_exception=True)
    refresh = RefreshToken.for_user(request.user)
    return Response(
        {"access": str(refresh.access_token), "refresh": str(refresh)},
        status=status.HTTP_200_OK,
    )
