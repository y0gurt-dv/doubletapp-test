from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from pets.serializers import pet as serializers
from pets.models.pet import Pet
from rest_framework.parsers import (FileUploadParser, FormParser,
                                    MultiPartParser)
from pets.filters.pet import PetFilter
from pets.services import pet as pet_services


class PetListCreateDeleteView(ListCreateAPIView):
    queryset = Pet.objects.prefetch_related('photos').all()
    serializer_class = serializers.PetCreateSerializer
    filterset_class = PetFilter

    def delete(self, request, *args, **kwargs):
        serializer = serializers.DeletePetsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = pet_services.many_delete_pets(serializer.data['ids'])
        return Response(result, status=status.HTTP_204_NO_CONTENT)


class AddPhotoToPetView(CreateAPIView):
    serializer_class = serializers.AddPhotoToPetSerializer
    parser_classes = (MultiPartParser, FileUploadParser, FormParser)
