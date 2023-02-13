#!/usr/bin/python3

import unittest
from models.state import State


class TestState(unittest.TestCase):

    # test class `State`

    def test_to_dict_state(self):
        state = State("test")
        self.assertEqual(type(state.to_dict()), dict)

    def test_from_dict_to_instace_state(self):
        state = State("test")
        state.from_dict_to_instace(state.to_dict())

    def test_from_dict_to_json_string_state(self):
        state = State("test")
        self.assertEqual(
            type(
                state.from_dict_to_json_string(
                    state.to_dict())),
            str)

    def test_from_json_string_to_dict_state(self):
        state = State("test")
        self.assertEqual(
            type(
                state.from_json_string_to_dict(
                    state.from_dict_to_json_string(
                        state.to_dict()))),
            dict,
        )

    def test_from_json_string_to_file_state(self):
        state = State("test")
        json_string = state.from_dict_to_json_string(
            state.to_dict())
        filename = "state.json"
        state.from_json_string_to_file(json_string, filename)
        with open(filename, "r") as f:
            self.assertEqual(json_string, f.read())

        # os.remove(filename)

    def test_from_file_to_json_string_state(self):
        state = State("test")
        self.assertEqual(
            type(
                state.from_file_to_json_string("state.json")),
            str)
