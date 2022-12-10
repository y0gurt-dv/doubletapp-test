import django_filters
from pets.models.pet import Pet
from django.db import models


class PetFilter(django_filters.FilterSet):
    has_photos = django_filters.BooleanFilter(method='has_photo_filter')

    def has_photo_filter(self, queryset, name, value):
        print(value)
        if value is None:
            return queryset

        if value:
            queryset = queryset.filter(~models.Q(photos=None))
        else:
            queryset = queryset.filter(photos=None)
        return queryset

    class Meta:
        model = Pet
        fields = [
            'has_photos'
        ]
