from django.core.management.base import BaseCommand
from mixer.backend.django import mixer

from mainapp.models import Person


class Command(BaseCommand):

    def handle(self, *args, **options):
        Person.objects.all().delete()
        for _ in range(20):
            mixer.blend(Person)
        print('done')
