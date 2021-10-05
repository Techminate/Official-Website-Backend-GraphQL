from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from apis.models.tasks import Tasks

class TasksNode(DjangoObjectType):
    class Meta:
        model = Tasks
        filter_fields = {
            'title':['exact', 'icontains', 'istartswith'],
            'job': ['exact']
        }
        interfaces = (relay.Node, )

class readTask:
    def getAll():
        return Tasks.objects.all()
    
    def getById(id):
       return Tasks.objects.get(pk=id)

class writeTask:
    def add(data):
        return Tasks(title=data[0])

class resText:
    def message(message):
        return f"{message}"