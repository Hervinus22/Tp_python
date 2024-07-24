import json
from django.core.management.base import BaseCommand
from employees.models import Employee

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        with open(json_file, 'r') as file:
            data = json.load(file)
            for item in data:
                Employee.objects.update_or_create(
                    ID=item['ID '],
                    defaults={
                        'anciennete': item['Anciennété'],
                        'experience': item['Experience'],
                        'paiement': item['Paiement'],
                        'departement': item['Departement'],
                        'evaluation': item['Evalutaion'],
                    }
                )
            self.stdout.write(self.style.SUCCESS('Successfully imported employees'))
