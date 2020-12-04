from django.core.management.base import BaseCommand, CommandError
from apiapp.models import Customer
import pandas as pd
import googlemaps
from tqdm import tqdm
from project_demo.settings import GCP_API_KEY


class Command(BaseCommand):
    help = 'import customers to database and add latitud and longitud to each one by address field '
    gmaps = googlemaps.Client(
        key=GCP_API_KEY)

    def add_arguments(self, parser):
        parser.add_argument('pathfile', type=str)

    def handle(self, *args, **options):
        pathfile = options["pathfile"]
        customers = pd.read_csv(pathfile, index_col=0)
        customers = customers.to_dict(orient='records')
        self.stdout.write(self.style.SUCCESS(
            "Requesting lat and log from Google Places API"))
        customers = [Customer(**self.put_geometry(customer))
                     for customer in tqdm(customers)]
        self.stdout.write(self.style.SUCCESS("Uploading bulk to database"))
        _ = Customer.objects.bulk_create(customers)
        self.stdout.write(self.style.SUCCESS(
            'Successfully loaded "%s"' % pathfile))

    def put_geometry(self, customer):
        geo_result = self.gmaps.find_place(
            input_type="textquery", input=customer["city"], fields=["geometry"])
        if geo_result["status"] == "OK":
            customer["latitude"] = geo_result["candidates"][0]["geometry"]["location"]["lat"]
            customer["longitude"] = geo_result["candidates"][0]["geometry"]["location"]["lng"]

        return customer
