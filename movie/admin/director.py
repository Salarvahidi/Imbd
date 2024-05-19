from django.contrib import admin
from movie.models import Director


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
