from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    """
    Django command for creating a superuser when User in db count 0
    """

    def handle(self, *args, **options):
        if get_user_model().objects.count() == 0:
            self.stdout.write('Create a new superuser...')
            user = get_user_model().objects.create_superuser(
                email='admin@gmail.com',
                password='admin'
            )
            user.save()
            self.stdout.write(
                self.style.SUCCESS('Superuser has been created!')
            )
        else:
            self.stdout.write('superuser is exist on db')
