import strawberry
import strawberry_django
from strawberry_django.optimizer import DjangoOptimizerExtension

from .types import Member


@strawberry.type
class Query:
    members: list[Member] = strawberry_django.field()


schema = strawberry.Schema(
    query=Query,
    extensions=[
        DjangoOptimizerExtension,
    ],
)
