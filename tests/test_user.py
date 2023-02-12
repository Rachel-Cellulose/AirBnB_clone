import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_to_dict_user(self):
        user = User("test", "test", "test", "test")
        self.assertEqual(type(user.to_dict()), dict)

    def test_from_dict_to_instace_user(self):
        user = User("test", "test", "test", "test")
        user.from_dict_to_instace(user.to_dict())

    def test_from_dict_to_json_string_user(self):
        user = User("test", "test", "test", "test")
        self.assertEqual(
            type(
                user.from_dict_to_json_string(
                    user.to_dict())),
            str)

    def test_from_json_string_to_dict_user(self):
        user = User("test", "test", "test", "test")
        self.assertEqual(
            type(
                user.from_json_string_to_dict(
                    user.from_dict_to_json_string(user.to_dict())
                )
            ),
            dict,
        )

    def test_from_json_string_to_file_user(self):
        user = User("test", "test", "test", "test")
        json_string = user.from_dict_to_json_string(
            user.to_dict())
        filename = "user.json"
        user.from_json_string_to_file(json_string, filename)
        with open(filename, "r") as f:
            self.assertEqual(json_string, f.read())

        # os.remove(filename)

    def test_from_file_to_json_string_user(self):
        user = User("test", "test", "test", "test")
        self.assertEqual(type(user.from_file_to_json_string("file.json")), str)
