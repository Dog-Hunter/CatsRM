from pymongo.collection import Collection
from datetime import datetime

class Document:
    def __init__(self,
                 _id = None,
                 _collection: Collection = None,
                 _timestamp: datetime = datetime.now()
                 ) -> None:
        self._id = _id
        self._collection = _collection
        self._timestamp = _timestamp

    def write(self):
        data = self.generate_json()      
        self._id = self._collection.insert_one(data).inserted_id

    def read(self, type, value):
        data = self._collection.find_one({f"{type}": value})
        self.__dict__.update(data)

    def generate_json(self):
        return dict((key, value) for key, value in self.__dict__.items() 
                    if not callable(value) and not key.startswith('__') and value is not None)