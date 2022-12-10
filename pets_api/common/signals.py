from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os
from common.models.file import File
from django.core.exceptions import ObjectDoesNotExist


@receiver(post_delete, sender=File)
def delete_file_on_delete(sender, instance, **kwargs):
    file = instance.file
    if os.path.isfile(file.path):
        parent_folder = file.path[:file.path.rindex('\\')]
        os.remove(file.path)
        os.rmdir(parent_folder)


@receiver(pre_save, sender=File)
def delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_instance: File = File.objects.get(pk=instance.pk)
        old_file = old_instance.file
    except ObjectDoesNotExist:
        return False

    new_file = instance.file
    if not old_instance == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
