from apis.schemas.repositories.messege import *
import graphene
from graphene import ObjectType

#Create data
class messegeCreate(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        address = graphene.String(required=True)
        messege = graphene.String(required=True)
        
    messege = graphene.Field(MessegeType)

    @classmethod
    def mutate(cls, root, info, name, email, phone, address, messege):
        messege = Messege(name=name, email=email, phone=phone, address=address, messege=messege)
        messege.save()
        return messegeCreate(messege=messege)


class Mutation(graphene.ObjectType):
    create_messege = messegeCreate.Field()