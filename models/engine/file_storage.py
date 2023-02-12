import json


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
            dict[key] = value.to_dict()
        json.dumps(dict)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                objects_dict = json.load(f)
                for key in objects_dict:
                    class_name, obj_id = key.split(".")
                    self.__objects[key] = eval(class_name)(**objects_dict[key])
        except FileNotFoundError:
            pass
