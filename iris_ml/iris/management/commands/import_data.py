# prediction/management/commands/import_iris_data.py
import csv
import os
from django.core.management.base import BaseCommand
from iris.models import IrisData


class Command(BaseCommand):
    help = "Load Iris data from CSV file into the database"

    def handle(self, *args, **kwargs):
        # Define the path to the CSV file
        csv_file_path = os.path.join("data", "iris.csv")

        # Read and import the CSV data
        with open(csv_file_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                IrisData.objects.create(
                    sepal_length=row["sepal_length"],
                    sepal_width=row["sepal_width"],
                    petal_length=row["petal_length"],
                    petal_width=row["petal_width"],
                    species=row["species"],
                )
        self.stdout.write(self.style.SUCCESS("Successfully imported data"))
