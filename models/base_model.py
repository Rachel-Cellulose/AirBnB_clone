#!/usr/bin/python3

import json
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.id}) {self.__dict__}"

    def from_instance_to_dict(self) -> dict:
        return self.__dict__

    def from_dict_to_instace(self, dict):
        for key, value in dict.items():
            setattr(self, key, value)

    def from_dict_to_json_string(self, dict):
        return json.dumps(dict)

    def from_json_string_to_dict(self, json_string):
        return json.loads(json_string)

    def from_json_string_to_file(self, json_string, filename):
        with open(filename, "w") as f:
            f.write(json_string)

    def from_file_to_json_string(self, filename):
        with open(filename, "r") as f:
            return f.read()
