import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def test_from_instance_to_dict_place(self):
        place = Place(
            "test", "test", "test", "test", 1, 1, 1, 1, 1, 1, ["test"]
        )  # noqa: E501
        self.assertEqual(type(place.from_instance_to_dict()), dict)

    def test_from_dict_to_instace_place(self):
        place = Place("test", "test", "test", "test", 1, 1, 1, 1, 1, 1, ["test"])  # noqa: E501
        place.from_dict_to_instace(place.from_instance_to_dict())
        self.assertEqual(type(place), Place)

    def test_from_dict_to_json_string_place(self):
        place = Place(
            "test",
            "test",
            "test",
            "test",
            1,
            1,
            1,
            1,
            1,
            1,
            ["test"])
        self.assertEqual(
            type(
                place.from_dict_to_json_string(
                    place.from_instance_to_dict())),
            str)

    def test_from_json_string_to_dict_place(self):
        place = Place(
            "test",
            "test",
            "test",
            "test",
            1,
            1,
            1,
            1,
            1,
            1,
            ["test"])
        self.assertEqual(
            type(
                place.from_json_string_to_dict(
                    place.from_dict_to_json_string(
                        place.from_instance_to_dict()))),
            dict,
        )

    def test_from_json_string_to_file_place(self):
        place = Place(
            "test",
            "test",
            "test",
            "test",
            1,
            1,
            1,
            1,
            1,
            1,
            ["test"])
        json_string = place.from_dict_to_json_string(
            place.from_instance_to_dict())
        filename = "place.json"
        place.from_json_string_to_file(json_string, filename)
        with open(filename, "r") as f:
            self.assertEqual(f.read(), json_string)
