from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from apis.models.jobs import Jobs

class JobsType(DjangoObjectType):
    class Meta:
        model = Jobs
        fields = ("id", "projectName", "title", "description", "requirements", "deadline")

class JobNode(DjangoObjectType):
    class Meta:
        model = Jobs
        filter_fields = {
            'projectName':['exact', 'icontains', 'istartswith'],
            'title':['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )

class readData:
    def getAll():
        return Jobs.objects.all()
    
    def getById(id):
       return Jobs.objects.get(pk=id)

class writeData:
    def add(data):
        return Jobs(projectName=data[0])

class resText:
    def success(message):
        return message
    
    def failed(message):
        return message