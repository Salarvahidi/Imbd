from django.db import models
from django.utils.translation import gettext_lazy as _


class Movie(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    year = models.IntegerField(verbose_name=_("Year"))
    director = models.ForeignKey(
        "movie.Director",
        on_delete=models.SET_NULL,
        verbose_name=_("Director"),
        blank=True,
        null=True,
    )
    rate = models.IntegerField(default=10, verbose_name=_("Rate"))

    def __str__(self):
        return f"{self.name} - {self.year}"

    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")
