from rest_framework import serializers
from common.models.file import File


class FileProfileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    def get_url(self, obj: File):
        return obj.get_absolute_url(self.context['request'])

    class Meta:
        model = File
        fields = [
            'id',
            'url'
        ]


class FileCreateSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)
    url = serializers.SerializerMethodField(read_only=True)

    def get_url(self, obj: File):
        return obj.get_absolute_url(self.context['request'])

    class Meta:
        model = File
        fields = [
            'id',
            'file',
            'url'
        ]
