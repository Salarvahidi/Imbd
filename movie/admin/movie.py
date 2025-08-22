from django.contrib import admin
from movie.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "year")
    list_filter = "year"
