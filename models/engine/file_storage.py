#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    -These serializes instances to JSON
    -These deserializes JSON to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        objClassName = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objClassName, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dict = FileStorage.__objects
        objdict = {obj: obj_dict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """
        If the file doesn't exist no exception should be raised.
        Deserializes the JSON file to __objects only if JSON file exists
        Otherwise, do nothing.
        """

        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    className = o["__class__"]
                    del o["__class__"]
                    self.new(eval(clssName)(**o))
        except FileNotFoundError:
            return
