from apis.schemas.repositories.jobs import *

import graphene
from graphene import ObjectType

#Create data
class jobCreate(graphene.Mutation):
    class Arguments:
        projectName = graphene.String(required=True)
        
    job = graphene.Field(JobsType)

    @classmethod
    def mutate(cls, root, info, projectName):
        data = (projectName)
        job = writeData.add(data)
        job.save()
        return jobCreate(job=job)

#Update data
class jobUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        projectName = graphene.String(required=True)

    job = graphene.Field(JobsType)

    @classmethod
    def mutate(cls, root, info, id, projectName):
        try:
            job = readData.getById(id)
            job.projectName = projectName
            job.save()
            return jobUpdate(job=job)
        except:
            return None

#Delete data
class jobDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        
    job = graphene.Field(JobsType)

    @classmethod
    def mutate(cls, root, info, id):
        try:
            job = readData.getById(id)
            job.delete()
            return resText.success("Successfully Done")
        except:
            return resText.failed("Failed")

class Mutation(graphene.ObjectType):
    create_job = jobCreate.Field()
    update_job = jobUpdate.Field()
    delete_job = jobDelete.Field()