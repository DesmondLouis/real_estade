import graphene

import listings.schema


class Query(listings.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
