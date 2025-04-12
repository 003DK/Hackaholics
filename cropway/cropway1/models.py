from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    soil_type = models.CharField(max_length=100)
    water_availability = models.CharField(max_length=50)
    expected_yield = models.CharField(max_length=100, blank=True, null=True)
    total_cost = models.IntegerField(blank=True, null=True)
    usage = models.TextField(blank=True, null=True)
    disadvantages = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
