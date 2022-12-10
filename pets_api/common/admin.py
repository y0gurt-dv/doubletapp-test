from django.contrib import admin
from common.models.file import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']
