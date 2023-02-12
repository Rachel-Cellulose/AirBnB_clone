#!/usr/bin/python3

# UNIT TESTS

import os
import unittest
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    # File Storage Test
    def test_all(self):
        storage = FileStorage()
        self.assertEqual(type(storage.all()), dict)

    def test_new(self):
        storage = FileStorage()
        storage.new(User("test@email.com", "test", "test", "test"))
        self.assertEqual(type(storage.all()), dict)

    def test_save(self):
        storage = FileStorage()
        storage.new(User("test@email.com", "test", "test", "test"))
        storage.save()
        self.assertEqual(type(storage.all()), dict)

    def test_reload(self):
        storage = FileStorage()
        storage.reload()
        self.assertEqual(type(storage.all()), dict)

    # test class `Place`
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

        # os.remove(filename)

    # test class `User`

    def test_from_instance_to_dict_user(self):
        user = User("test", "test", "test", "test")
        self.assertEqual(type(user.from_instance_to_dict()), dict)

    def test_from_dict_to_instace_user(self):
        user = User("test", "test", "test", "test")
        user.from_dict_to_instace(user.from_instance_to_dict())

    def test_from_dict_to_json_string_user(self):
        user = User("test", "test", "test", "test")
        self.assertEqual(
            type(
                user.from_dict_to_json_string(
                    user.from_instance_to_dict())),
            str)

    def test_from_json_string_to_dict_user(self):
        user = User("test", "test", "test", "test")
        self.assertEqual(
            type(
                user.from_json_string_to_dict(
                    user.from_dict_to_json_string(user.from_instance_to_dict())
                )
            ),
            dict,
        )

    def test_from_json_string_to_file_user(self):
        user = User("test", "test", "test", "test")
        json_string = user.from_dict_to_json_string(
            user.from_instance_to_dict())
        filename = "user.json"
        user.from_json_string_to_file(json_string, filename)
        with open(filename, "r") as f:
            self.assertEqual(json_string, f.read())

        # os.remove(filename)

    def test_from_file_to_json_string_user(self):
        user = User("test", "test", "test", "test")
        self.assertEqual(type(user.from_file_to_json_string("file.json")), str)

    # test class `State`
    def test_from_instance_to_dict_state(self):
        state = State("test")
        self.assertEqual(type(state.from_instance_to_dict()), dict)

    def test_from_dict_to_instace_state(self):
        state = State("test")
        state.from_dict_to_instace(state.from_instance_to_dict())

    def test_from_dict_to_json_string_state(self):
        state = State("test")
        self.assertEqual(
            type(
                state.from_dict_to_json_string(
                    state.from_instance_to_dict())),
            str)

    def test_from_json_string_to_dict_state(self):
        state = State("test")
        self.assertEqual(
            type(
                state.from_json_string_to_dict(
                    state.from_dict_to_json_string(
                        state.from_instance_to_dict()))),
            dict,
        )

    def test_from_json_string_to_file_state(self):
        state = State("test")
        json_string = state.from_dict_to_json_string(
            state.from_instance_to_dict())
        filename = "state.json"
        state.from_json_string_to_file(json_string, filename)
        with open(filename, "r") as f:
            self.assertEqual(json_string, f.read())

        # os.remove(filename)

    def test_from_file_to_json_string_state(self):
        state = State("test")
        self.assertEqual(
            type(
                state.from_file_to_json_string("file.json")),
            str)

    # test class `City`
    def test_from_instance_to_dict_city(self):
        city = City("test", "test")
        self.assertEqual(type(city.from_instance_to_dict()), dict)

    def test_from_dict_to_instace_city(self):
        city = City("test", "test")
        city.from_dict_to_instace(city.from_instance_to_dict())

    def test_from_dict_to_json_string_city(self):
        city = City("test", "test")
        self.assertEqual(
            type(
                city.from_dict_to_json_string(
                    city.from_instance_to_dict())),
            str)

    def test_from_json_string_to_dict_city(self):
        city = City("test", "test")
        self.assertEqual(
            type(
                city.from_json_string_to_dict(
                    city.from_dict_to_json_string(city.from_instance_to_dict())
                )
            ),
            dict,
        )

    def test_from_json_string_to_file_city(self):
        city = City("test", "test")
        json_string = city.from_dict_to_json_string(
            city.from_instance_to_dict())
        filename = "city.json"
        city.from_json_string_to_file(json_string, filename)
        with open(filename, "r") as f:
            self.assertEqual(json_string, f.read())

        # os.remove(filename)

    def test_from_file_to_json_string_city(self):
        city = City("test", "test")
        self.assertEqual(type(city.from_file_to_json_string("file.json")), str)

    # test class `Amenity`
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

    # test class `Review`

    def test_from_instance_to_dict_review(self):
        review = Review("test", "test", "test")
        self.assertEqual(type(review.from_instance_to_dict()), dict)

    def test_from_dict_to_instace_review(self):
        review = Review("test", "test", "test")
        review.from_dict_to_instace(review.from_instance_to_dict())

    def test_from_dict_to_json_string_review(self):
        review = Review("test", "test", "test")
        self.assertEqual(
            type(
                review.from_dict_to_json_string(
                    review.from_instance_to_dict())),
            str)

    def test_from_json_string_to_dict_review(self):
        review = Review("test", "test", "test")
        self.assertEqual(
            type(
                review.from_json_string_to_dict(
                    review.from_dict_to_json_string(
                        review.from_instance_to_dict()))),
            dict,
        )

    def test_from_json_string_to_file_review(self):
        review = Review("test", "test", "test")
        json_string = review.from_dict_to_json_string(
            review.from_instance_to_dict())
        filename = "review.json"
        review.from_json_string_to_file(json_string, filename)
        with open(filename, "r") as f:
            self.assertEqual(json_string, f.read())

        # os.remove(filename)

    def test_from_file_to_json_string_review(self):
        review = Review("test", "test", "test")
        self.assertEqual(
            type(
                review.from_file_to_json_string("file.json")),
            str)


# create base_model.py
# create
