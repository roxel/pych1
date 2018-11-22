import json
import graphene

from graphene_django import DjangoObjectType
from graphene_django.converter import convert_django_field

from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

from places.models import Place, Category, Rating
User = get_user_model()


# scalar type for location

class GeoJSON(graphene.Scalar):
    @classmethod
    def serialize(cls, value):
        return json.loads(value.geojson)


@convert_django_field.register(models.GeometryField)
def convert_field_to_geojson(field, registry=None):
    return graphene.Field(GeoJSON, description=field.help_text, required=not field.null)


# object types and queries

class UserType(DjangoObjectType):
    class Meta:
        model = User


class PlaceType(DjangoObjectType):
    location = graphene.String()

    class Meta:
        model = Place

    def resolve_location(self, info):
        return '({}, {})'.format(self.location.x, self.location.y)


class RatingType(DjangoObjectType):
    class Meta:
        model = Rating


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


# main query

class PlaceQuery(graphene.ObjectType):
    users = graphene.List(UserType)
    places = graphene.List(PlaceType)
    ratings = graphene.List(RatingType)
    categories = graphene.List(CategoryType)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_places(self, info):
        return Place.objects.all()

    def resolve_categories(self, info):
        return Category.objects.all()

    def resolve_ratings(self, info):
        return Rating.objects.all()
