from django.core.management.base import BaseCommand
import csv
from plant.models import Plant

class Command(BaseCommand):
    help = 'Import data from a CSV file into the Plant model'

    def handle(self, *args, **options):
        csv_file_path = r'C:\Users\sifti\OneDrive\Desktop\capb\plant_dataset.csv'

        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Plant.objects.create(
                    plant_name= row['plant_name'],
                    pot_size = row['pot_size'],
                    n = row['n'],
                    p = row['p'],
                    k = row['k'],
                    co2 = row['co2'],
                    ph = row['ph'],
                    ec = row['ec'],
                    moisture = row['moisture'],
                    humidity = row['humidity'],
                    temperature = row['temperature'],
                    soil_type = row['soil_type'],
                    rainfall  = row['rainfall'],
                    sunlight = row['sunlight'],
                    sunlight_type  = row['sunlight_type'],
                    season  = row['season'],
                    watering   = row['watering'],
                    plant_type   = row['plant_type'],
                    
                    
                   
                )

        self.stdout.write(self.style.SUCCESS('Data import from CSV completed.'))
