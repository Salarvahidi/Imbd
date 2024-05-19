from django.contrib import admin
from django.urls import path, include

from user.urls import user_urlpatterns
from movie.urls import movie_urlpatterns

api_urlpatterns = [
    path("user/", include(user_urlpatterns), name="user"),
    path("movie/", include(movie_urlpatterns), name="movie"),
]

urlpatterns = [path("admin/", admin.site.urls), path("api/", include(api_urlpatterns))]
