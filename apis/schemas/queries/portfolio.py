from apis.schemas.repositories.portfolio import *
import graphene

class Query(graphene.ObjectType):
    all_portfolio = graphene.List(PortfolioType)
    def resolve_all_portfolio(root, info):
        return Portfolio.objects.all()

    portfolio_byId = graphene.Field(PortfolioType, id=graphene.Int())
    def resolve_portfolio_byId(root, info, id):
        return Portfolio.objects.get(pk=id)
