from django.db import models
from common.models.mixins.date import DateMixin
from common.models.mixins.id import IdMixin


class Pet(IdMixin, DateMixin):
    PET_TYPES = (
        ('dog', 'dog'),
        ('cat', 'cat'),
    )

    name = models.CharField("Name", max_length=128)
    age = models.IntegerField("Age")
    type = models.CharField(
        "Type",
        max_length=50,
        choices=PET_TYPES
    )
    photos = models.ManyToManyField(
        "common.File",
        verbose_name="Photos",
        blank=True
    )

    def __str__(self):
        return 'id: {}'.format(
            self.id,
        )

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'
