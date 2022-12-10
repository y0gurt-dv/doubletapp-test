from django.contrib import admin
from pets.models.pet import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'type']
    list_filter = ['type', ]
    search_fields = ['name', ]
    filter_vertical = ['photos', ]
