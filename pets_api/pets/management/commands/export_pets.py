# from django.core.management.base import BaseCommand
# from pets.models.pet import Pet
# from django.db import models
# from pets.serializers.pet import PetsForExportSerializer


# class Command(BaseCommand):
#     help = 'Export pets'

#     def add_arguments(self, parser):
#         parser.add_argument('--has-photos', type=bool)

#     def handle(self, *args, **options):
#         pets = Pet.objects.prefetch_related('photos').all()
#         has_photos = options['has_photos']

#         print(pets, has_photos)

#         if has_photos is True:
#             pets = pets.filter(~models.Q(photos=None))
#         elif has_photos is False:
#             pets = pets.filter(photos=None)

#         serializer = PetsForExportSerializer(pets, many=True)

#         self.stdout.write(str(serializer.data))
