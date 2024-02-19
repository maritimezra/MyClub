import strawberry_django
from strawberry import auto

from . import models


@strawberry_django.type(models.Member)
class Member:
    id: auto
    first_name: str
    last_name: str
    email: str
