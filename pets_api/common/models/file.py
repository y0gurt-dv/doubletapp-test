from django.db import models
from common.models.mixins.date import DateMixin
from common.models.mixins.id import IdMixin
from rest_framework.exceptions import ParseError


def get_file_dir(i, f):
    return f'{i.id}/{f}'


class File(IdMixin, DateMixin):
    file = models.FileField(
        upload_to=get_file_dir
    )

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self, request=None):
        if request is None:
            print('Empty request')
            return None
        try:
            file_url = self.file.url
            return request.build_absolute_uri(file_url)
        except Exception as e:
            raise ParseError(e)
