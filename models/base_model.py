#!/usr/bin/python3
from datetime import datetime
import uuid
from models import storage

class BaseModel:
    """Defines all common attributes/methods for other classess"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        storage.new()

    def __str__(self):
        """Returns classname, id and dict"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all key/values of __dict__ instance"""
        classname = self.__class__.__name__
        updated_dict = self.__dict__.copy()
        updated_dict['__class__'] = classname
        updated_dict['created_at'] = self.created_at.isoformat()
        updated_dict['updated_at'] = self.updated_at.isoformat()
        return updated_dict
