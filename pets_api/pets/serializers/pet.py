from rest_framework import serializers
from pets.models.pet import Pet
from common.serializers import file as file_serializers
from common.serializers.mixins import ParseContextSerializerMixin
from django.db import transaction
from django.conf import settings


class PetProfileSerializer(serializers.ModelSerializer):
    photos = file_serializers.FileProfileSerializer(many=True)

    class Meta:
        model = Pet
        fields = '__all__'


class PetCreateSerializer(serializers.ModelSerializer):
    photos = file_serializers.FileProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Pet
        fields = '__all__'


class AddPhotoToPetSerializer(file_serializers.FileCreateSerializer,
                              ParseContextSerializerMixin):

    @transaction.atomic
    def create(self, validated_data):
        new_file = super().create(validated_data)
        pet = self._get_obj_from_context(
            context_field='id',
            context_model=Pet
        )

        pet.photos.add(new_file)

        return new_file


class DeletePetsSerializer(serializers.Serializer):
    ids = serializers.ListField(
        child=serializers.UUIDField()
    )
