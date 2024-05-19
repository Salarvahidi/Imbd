from django.urls import path, include
from rest_framework import routers

from user import views

router = routers.DefaultRouter()
router.register(r"user", views.UserViewSet)


user_urlpatterns = [
    path("", include(router.urls)),
]
