from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from movie.serializers.director import DirectorSerializer
from movie.models import Director


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.order_by("-id")
    permission_classes = [IsAuthenticated]
    serializer_class = DirectorSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = "__all__"
