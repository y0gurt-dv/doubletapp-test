from rest_framework.authentication import BaseAuthentication
from django.http import HttpRequest
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed


class APIKeyAuthentication(BaseAuthentication):
    def get_key(self, request: HttpRequest) -> str:
        header_field = settings.API_KEY_HEADER
        return request.META.get(header_field)

    def authenticate(self, request: HttpRequest):
        key = self.get_key(request)
        if not key or not settings.ACCESS_API_KEY == key:
            raise AuthenticationFailed()

    def authenticate_header(self, request):
        return 'WWW-Authenticate'
