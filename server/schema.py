import graphene

# queries
import apis.schemas.queries.jobs

# mutations
import apis.schemas.mutations.jobs

class Query(
    apis.schemas.queries.jobs.Query,
    graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(
    apis.schemas.mutations.jobs.Mutation,
    graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)