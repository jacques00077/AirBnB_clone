#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    This handles the various places available
    - Attributes
        - city_id: (str) -> City.id
        - user_id: (str) -> User.id
        - name: (str)
        - description: (str)
        - number_rooms: (int)
        - number_bathrooms: (int)
        - max_guest: (int)
        - price_by_night: (int)
        - latitude: (float)
        - longitude: (float)
        - amenity_ids: (list) -> Amenity.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
