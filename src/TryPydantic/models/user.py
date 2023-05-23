"""User models."""
from pydantic import BaseModel


class User (BaseModel):
    """User model."""

    id: int
    name = 'Jane Doe'
