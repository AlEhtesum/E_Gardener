from django.db import models


class Plant(models.Model):
    plant_name = models.CharField(max_length=100)
    pot_size = models.IntegerField()
    n = models.CharField(max_length=50)
    p = models.CharField(max_length=50)
    k = models.CharField(max_length=50)
    co2 = models.CharField(max_length=50)
    ph = models.CharField(max_length=50)
    ec = models.CharField(max_length=50)
    moisture = models.CharField(max_length=50)
    humidity = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)
    soil_type = models.CharField(max_length=50)
    rainfall = models.CharField(max_length=50)
    sunlight = models.CharField(max_length=50)
    sunlight_type = models.CharField(max_length=50)
    season = models.CharField(max_length=50)
    watering = models.CharField(max_length=50)
    plant_type = models.CharField(max_length=50)
    plant_description = models.TextField(null=True)
    plant_image = models.ImageField(upload_to="plants/", null=True)

    def __str__(self):
        return self.plant_name

    class Meta:
        ordering = ["plant_name"]
