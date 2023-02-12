import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_from_instance_to_dict_amenity(self):
        amenity = Amenity("test")
        self.assertEqual(type(amenity.from_instance_to_dict()), dict)

    def test_from_dict_to_instace_amenity(self):
        amenity = Amenity("test")
        amenity.from_dict_to_instace(amenity.from_instance_to_dict())

    def test_from_dict_to_json_string_amenity(self):
        amenity = Amenity("test")
        self.assertEqual(
            type(
                amenity.from_dict_to_json_string(
                    amenity.from_instance_to_dict())),
            str)

    def test_from_file_to_json_string_amenity(self):
        amenity = Amenity("test")
        self.assertEqual(
            type(
                amenity.from_file_to_json_string("amenity.json")),
            str)

    def test_from_json_string_to_dict_amenity(self):
        amenity = Amenity("test")
        self.assertEqual(
            type(
                amenity.from_json_string_to_dict(
                    amenity.from_dict_to_json_string(
                        amenity.from_instance_to_dict()))),
            dict,
        )

    def test_from_json_string_to_file_amenity(self):
        amenity = Amenity("test")
        json_string = amenity.from_dict_to_json_string(
            amenity.from_instance_to_dict())
        filename = "amenity.json"
        amenity.from_json_string_to_file(json_string, filename)
        with open(filename, "r") as f:
            self.assertEqual(json_string, f.read())

        # os.remove(filename)
