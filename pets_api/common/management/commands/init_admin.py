from django.core.management.base import BaseCommand
from pets.models.pet import Pet
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Admin init'

    def add_arguments(self, parser):
        parser.add_argument('--email', type=str, required=True)
        parser.add_argument('--username', type=str, required=True)
        parser.add_argument('--password', type=str, required=True)

    def handle(self, *args, **options):
        if User.objects.exists():
            self.stderr.write('User already exist')
            return
        
        User.objects.create_superuser(
            email=options['email'],
            username=options['username'],
            password=options['password'],
        )
        self.stdout.write('Successfully')
