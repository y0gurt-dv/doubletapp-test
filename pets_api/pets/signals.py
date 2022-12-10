from django.db.models.signals import pre_delete
from django.dispatch import receiver
from pets.models.pet import Pet


@receiver(pre_delete, sender=Pet)
def delete_file_on_delete_pet(sender, instance: Pet, **kwargs):
    print(instance)
    print(instance.photos.all())
    instance.photos.all().delete()
