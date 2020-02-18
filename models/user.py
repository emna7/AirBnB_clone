#!/usr/bin/python3
"""
Define: User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email (str): User email.
        password (str): User account password.
        first_name (str): User first name.
        last_name (str): User last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
