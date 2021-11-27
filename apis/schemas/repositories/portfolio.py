from graphene_django import DjangoObjectType

from apis.models.portfolio import Portfolio

class PortfolioType(DjangoObjectType):
    class Meta:
        model = Portfolio
        fields = ("id","category","title","image","link")
