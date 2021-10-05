from apis.schemas.repositories.jobs import *
from apis.schemas.repositories.tasks import *

import graphene
from graphene import ObjectType

class Query(ObjectType):

    job = relay.Node.Field(JobsNode)
    all_jobs = DjangoFilterConnectionField(JobsNode)

    task = relay.Node.Field(TasksNode)
    all_tasks = DjangoFilterConnectionField(TasksNode)