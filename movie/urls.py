from django.urls import path, include
from rest_framework import routers

from movie import views

router = routers.DefaultRouter()
router.register(r"movie", views.MovieViewSet)
router.register(r"director", views.DirectorViewSet)

movie_urlpatterns = [
    path("", include(router.urls)),
]
