from collections.abc import Iterator

from apps.users.models import Gamer
from apps.users.services import faker


def generate_user() -> Gamer:
    return Gamer(
        name=faker.unique.username(),
        email=faker.unique.company_email(),
        password=faker.unique.password()
    )


def generate_users(amount: int) -> Iterator[Gamer]:
    for _ in range(amount):
        yield generate_user()
