import graphene

# queries
import apis.schemas.queries.jobs
import apis.schemas.queries.members
import apis.schemas.queries.portfolio

# mutations
import apis.schemas.mutations.jobs
import apis.schemas.mutations.messege

class Query(
    apis.schemas.queries.jobs.Query,
    apis.schemas.queries.members.Query,
    apis.schemas.queries.portfolio.Query,
    graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(
    apis.schemas.mutations.jobs.Mutation,
    apis.schemas.mutations.messege.Mutation,
    graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)