import strawberry
import strawberry_django
from typing import List, Optional
from strawberry_django.optimizer import DjangoOptimizerExtension

from .models import Member
from .types import MemberType


@strawberry.type
class Query:

    @strawberry.field
    def get_members(self) -> List[MemberType]:
        return Member.objects.all()

    @strawberry.field
    def get_member_with_id(self, id: str) -> List[MemberType]:
        return Member.objects.filter(id=id)

    @strawberry.field
    def get_member_with_email(self, email: str) -> List[MemberType]:
        return Member.objects.filter(email=email)

    @strawberry.field
    def get_member_with_first_name(self, first_name: str) -> List[MemberType]:
        return Member.objects.filter(first_name=first_name)

    @strawberry.field
    def get_member_with_last_name(self, last_name: str) -> List[MemberType]:
        return Member.objects.filter(last_name=last_name)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_member(self, email: str, first_name: str, last_name: str) -> MemberType:
        member = Member.objects.create(
            email=email, first_name=first_name, last_name=last_name
        )
        return member

    @strawberry.mutation
    def update_member(self, email: str, first_name: str, last_name: str) -> MemberType:
        member = Member.objects.get(email=email)
        member.first_name = first_name
        member.last_name = last_name
        member.save()
        return member

    @strawberry.mutation
    def delete_member(self, email: str) -> MemberType:
        member = Member.objects.get(email=email)
        member.delete()
        return member


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        DjangoOptimizerExtension,
    ],
)
