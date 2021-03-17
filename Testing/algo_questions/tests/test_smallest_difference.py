from unittest import TestCase

from algo_questions.arrays.smallest_difference import get_smallest_difference


class SmallestDifferenceTests(TestCase):
    def test_smallest_difference(self):

        array_one = [-1, 5, 10, 20, 28, 3]
        array_two = [26, 134, 135, 15, 17]

        self.assertEqual(
            get_smallest_difference(array_one, array_two),
            [28, 26]
        )
