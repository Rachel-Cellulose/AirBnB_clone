from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self) -> None:
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        dict = {}
        for key, value in self.__objects.items():
            dict[key] = value.from_instance_to_dict()
        BaseModel().from_dict_to_json_string(dict)

    def reload(self):
        pass
