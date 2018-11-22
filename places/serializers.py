from django.contrib.auth import get_user_model
from rest_framework import serializers

from places.fields import LocationField
from places.models import Category, Place, Rating


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        exclude = ()


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    location = LocationField()

    class Meta:
        model = Place
        exclude = ()
