from django.db import models
from django.utils.translation import gettext_lazy as _


class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Director name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Director last name"))
    birth_date = models.DateField(verbose_name=_("Director birth date"))
    is_active = models.BooleanField(default=True, verbose_name=(" Is active"))

    def __str__(self):
        return f"{self.name} - {self.last_name}"

    class Meta:
        verbose_name = _("Director")
        verbose_name_plural = _("Directors")
