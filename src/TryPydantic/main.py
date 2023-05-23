"""Simple function."""
from .models.user import User


def add_one(number):
    """Add 1 to `number`."""
    return number + 1


def create_user():
    """Create a user."""
    return User(
        id=123,
    )
