#!/usr/bin/python3
"""
The module for file storage
"""
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    -These serializes instances to JSON
    -These deserializes JSON to instances
    """

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        This sets an object in __objects with key <obj_class>.id
        """
        objClassName = obj.__class__.__name__
        key = "{}.{}".format(objClassName, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """It returns dictionary of objects"""
        return FileStorage.__objects
    def save(self):
        """
        These serializes __objects into JSON file (path __file_path)
        """
        obj_dict = {}
        for key, obj in self.all().items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="UTF-8") as text_file:
            json.dump(obj_dict, text_file)

    def reload(self):
        """
        If the file doesn't exist no exception should be raised.
	Deserializes the JSON file to __objects only if JSON file exists
        Otherwise do nothing.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        from models.state import State

        # Import others as needed and add to the calss map dictionary below

        class_map = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'City': City,
                    'Place': Place,
                    'State': State,
                    'Amenity': Amenity,
                    'Review': Review,
            }
        if os.path.isfile(FileStorage.__file_path):
           try:
               with open(FileStorage.__file_path, "r", encoding="UTF-8") as text_file:
                   obj_dict = json.load(text_file)

                   for key, val in obj_dict.items():
                       class_name = val['__class__']
                       class_instance = class_map[class_name]
                       instance = class_instance(**val)
                       all_objects = self.all()
                       FileStorage._objects[key] = instance
           except FileNotFoundError:
                   pass
