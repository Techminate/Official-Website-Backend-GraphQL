from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from apis.models.members import Team

class TeamNode(DjangoObjectType):
    class Meta:
        model = Team
        filter_fields = ['name']
        interfaces = (relay.Node, )

class readTask:
    def getAll():
        return Team.objects.all()
    
    def getById(id):
       return Team.objects.get(pk=id)

class resText:
    def message(message):
        return f"{message}"