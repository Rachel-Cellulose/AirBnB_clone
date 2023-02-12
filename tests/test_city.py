#!/usr/bin/python3

import unittest
from models.city import City


class TestCity(unittest.TestCase):

    # test class `City`
    def to_dict(self):
        city = City("test", "test")
        self.assertEqual(type(city.to_dict()), dict)

    def test_from_dict_to_instace_city(self):
        city = City("test", "test")
        city.from_dict_to_instace(city.to_dict())

    def test_from_dict_to_json_string_city(self):
        city = City("test", "test")
        self.assertEqual(
            type(
                city.from_dict_to_json_string(
                    city.to_dict())),
            str)

    def test_from_json_string_to_dict_city(self):
        city = City("test", "test")
        self.assertEqual(
            type(
                city.from_json_string_to_dict(
                    city.from_dict_to_json_string(city.to_dict())
                )
            ),
            dict,
        )

    def test_from_json_string_to_file_city(self):
        city = City("test", "test")
        json_string = city.from_dict_to_json_string(
            city.to_dict())
        filename = "city.json"
        city.from_json_string_to_file(json_string, filename)
        with open(filename, "r") as f:
            self.assertEqual(json_string, f.read())

        # os.remove(filename)

    def test_from_file_to_json_string_city(self):
        city = City("test", "test")
        self.assertEqual(type(city.from_file_to_json_string("city.json")), str)
