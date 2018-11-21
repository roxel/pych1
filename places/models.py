from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from django.core.validators import MinValueValidator, MaxValueValidator
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
    established = models.DateField(null=True, blank=True)
    location = PointField(default=Point(x=18.662252, y=50.291149))
    description = models.TextField(blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    value = models.IntegerField(validators=(MinValueValidator(0), MaxValueValidator(5)))
    comment = models.TextField(blank=True)
    added = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.value}/5"
