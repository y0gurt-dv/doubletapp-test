from django.db import transaction
from pets.models.pet import Pet


@transaction.atomic
def many_delete_pets(ids_list: list):
    pets = Pet.objects.filter(id__in=ids_list).all()
    pets_ids = pets.values_list('id', flat=True)

    pets_ids = {str(i) for i in pets_ids}
    ids_list = set(ids_list)

    diff_ids = pets_ids.symmetric_difference(ids_list)

    pets.delete()

    deleted = len(pets_ids)
    errors = [
        {
            'id': id,
            'error': 'Pet with the matching ID was not found.',
        } for id in diff_ids
    ]

    return {
        'deleted': deleted,
        'errors': errors
    }
