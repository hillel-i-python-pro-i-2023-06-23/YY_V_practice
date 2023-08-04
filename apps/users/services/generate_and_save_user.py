import logging

from apps.users.models import Gamer
from apps.users.services.generate_users import generate_users


def generate_and_save_user(amount: int):
    logger = logging.getLogger("django")

    queryset = Gamer.objects.all()

    logger.info(f"Current amount of contacts before: {queryset.count()}")

    for user in generate_users(amount=amount):
        user.save()

    logger.info(f"Current amount of contacts after: {queryset.count()}")
