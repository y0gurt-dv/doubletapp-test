from django.db import models


class DateMixin(models.Model):
    created_at = models.DateTimeField(verbose_name='Created at',
                                      auto_now_add=True)

    class Meta:
        abstract = True
