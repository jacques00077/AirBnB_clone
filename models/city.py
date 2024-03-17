#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A class to represent the various cities
    - Attributes
        - state_id: (str) -> State.id
        - name: (str)
    """

    state_id = ""
    name = ""
