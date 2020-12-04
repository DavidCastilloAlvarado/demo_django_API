from django.core.management.base import BaseCommand, CommandError
from apiapp.models import Customer
import pandas as pd


class Command(BaseCommand):
    help = 'import customers to database and add latitud and longitud to each one by address field '

    def add_arguments(self, parser):
        parser.add_argument('confirm', type=int)

    def handle(self, *args, **options):
        confirm = options["confirm"]
        if confirm == 1:
            ref = Customer.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(
                'Customer db deleted "%s"' % confirm))
        else:
            self.stdout.write(self.style.SUCCESS(
                'Customer db was not deleted "%s" "%s"' % confirm))
