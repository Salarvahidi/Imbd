from rest_framework.viewsets import ModelViewSet

from user.serializers.user import UserSerializer, MiniUserSerializer
from user.models.user import User

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(ModelViewSet):

    queryset = User.objects.order_by("-date_joined")
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = "__all__"
    permission_classes = [IsAuthenticated]

    @action(methods=["POST"], detail=False)
    def log_out(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
