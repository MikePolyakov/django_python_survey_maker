from django.core.management.base import BaseCommand
from mixer.backend.django import mixer

from constructor_app.models import Company


class Command(BaseCommand):

    def handle(self, *args, **options):
        count = 10
        for i in range(count):
            p = (i/count)*100
            print(f'{i}) {p} %')
            new_company = mixer.blend(Company)
            print(new_company)

        print('end')
