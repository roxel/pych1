from django.contrib.gis.geos import Point
from django.db import models
from django.contrib.gis.db.models import PointField


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Place(models.Model):
    name = models.CharField(max_length=500)
    location = PointField(default=Point(x=18.662252, y=50.291149))
    description = models.TextField(blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
