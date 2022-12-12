from django.core.management.base import BaseCommand
from pets.models.pet import Pet
from django.db import models
from django.conf import settings
import json


class Command(BaseCommand):
    help = 'Export pets'

    def add_arguments(self, parser):
        parser.add_argument('--has-photos', type=bool)

    def handle(self, *args, **options):
        pets = Pet.objects.prefetch_related('photos').all()
        has_photos = options['has_photos']
        host = settings.ALLOWED_HOSTS[0]

        if has_photos is True:
            pets = pets.filter(~models.Q(photos=None))
        elif has_photos is False:
            pets = pets.filter(photos=None)

        output = []
        for pet in pets:
            photos = [
                'https://{host}{url}'.format(host=host, url=photo.file.url)
                for photo in pet.photos.all()
            ]
            output.append({
                'id': str(pet.id),
                'name': pet.name,
                'age': pet.age,
                'type': pet.type,
                'photos': photos,
                'created_at': pet.created_at.isoformat()
            })


        self.stdout.write(json.dumps({'pets': output}))
