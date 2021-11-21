from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from apis.models.members import Member

class MemberNode(DjangoObjectType):
    class Meta:
        model = Member
        filter_fields = ['name']
        interfaces = (relay.Node, )

class readTask:
    def getAll():
        return Member.objects.all()
    
    def getById(id):
       return Member.objects.get(pk=id)

class resText:
    def message(message):
        return f"{message}"