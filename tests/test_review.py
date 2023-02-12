import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def test_to_dict_review(self):
        review = Review("test", "test", "test")
        self.assertEqual(type(review.to_dict()), dict)

    def test_from_dict_to_instace_review(self):
        review = Review("test", "test", "test")
        review.from_dict_to_instace(review.to_dict())

    def test_from_dict_to_json_string_review(self):
        review = Review("test", "test", "test")
        self.assertEqual(
            type(
                review.from_dict_to_json_string(
                    review.to_dict())),
            str)

    def test_from_json_string_to_dict_review(self):
        review = Review("test", "test", "test")
        self.assertEqual(
            type(
                review.from_json_string_to_dict(
                    review.from_dict_to_json_string(
                        review.to_dict()))),
            dict,
        )

    def test_from_json_string_to_file_review(self):
        review = Review("test", "test", "test")
        json_string = review.from_dict_to_json_string(
            review.to_dict())
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
