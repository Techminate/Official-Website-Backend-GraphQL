from apis.schemas.repositories.members import *
from apis.schemas.repositories.team import *

import graphene
from graphene import ObjectType

class Query(ObjectType):

    member = relay.Node.Field(MemberNode)
    all_members = DjangoFilterConnectionField(MemberNode)

    team = relay.Node.Field(TeamNode)
    all_team = DjangoFilterConnectionField(TeamNode)