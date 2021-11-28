from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from apis.models.messege import Messege

class MessegeType(DjangoObjectType):
    class Meta:
        model = Messege
        fields = ("id", "name", "email", "phone", "address", "messege")
