from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from movie.serializers.movie import MovieSerializer
from movie.models import Movie

from movie.task import send_email


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.order_by("-id")
    permission_classes = [IsAuthenticated]
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = "__all__"

    @action(methods=["GET"], detail=True)
    def rate(self, request, pk):
        request_rate = request.data["rate"]
        movie = self.get_object()
        movie.rate = (int(movie.rate) + int(request_rate)) / 2
        movie.save(update_fields=["rate"])
        user_email = request.user.email
        send_email.delay(user_email)
        return Response({"movie": MovieSerializer(movie).data})
