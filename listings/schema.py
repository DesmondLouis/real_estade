import graphene
from graphene_django import DjangoObjectType

from .models import Listing
from realtors.models import Realtor


class ListingType(DjangoObjectType):
    class Meta:
        model = Listing


class RealtorType(DjangoObjectType):
    class Meta:
        model = Realtor


class Query(graphene.ObjectType):
    listing = graphene.Field(ListingType, id=graphene.Int())
    realtor = graphene.Field(RealtorType, id=graphene.Int())
    listings = graphene.List(ListingType)
    realtors = graphene.List(RealtorType)

    def resolve_listings(self, info, **kwargs):
        return Listing.objects.all()

    def resolve_listing(selfs, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return Listing.objects.get(pk=id)
        return None

    def resolve_realtors(self, info, **kwargs):
        return Realtor.objects.all()

    def resolve_realtor(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return Realtor.objects.get(pk=id)
        return None

class RealtorInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    phone = graphene.String()
    description = graphene.String()
    photo = graphene.String()
    is_mvp = graphene.Boolean()
    hire_date = graphene.DateTime()

class CreateLink(graphene.Mutation):
    id = graphene.Int()
