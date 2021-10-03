from apis.schemas.repositories.jobs import *

import graphene
from graphene import ObjectType

class Query(ObjectType):

    all_jobs = graphene.List(JobsType)
    def resolve_all_jobs(root, info):
        try:
            return readData.getAll()
        except:
            return None

    details_job = graphene.Field(JobsType, id=graphene.Int())
    def resolve_details_job(root, info, id):
        try:
            return readData.getById(id)
        except:
            return None

    job = relay.Node.Field(JobNode)
    search_job = DjangoFilterConnectionField(JobNode)