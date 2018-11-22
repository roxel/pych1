import graphene

from places.schema import PlaceQuery


class Query(PlaceQuery):
    pass


schema = graphene.Schema(query=Query)
