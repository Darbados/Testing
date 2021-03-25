from unittest.case import TestCase

from algo_questions.arrays.is_array_monotonic import is_monotonic
from algo_questions.arrays.tests.test_smallest_difference import array_one, array_two


class IsArrayMonotonicTests(TestCase):
    def test_is_monotonic(self):
        self.assertFalse(is_monotonic(array_one))
        self.assertFalse(is_monotonic(array_two))

        array = [-1, -5, -10, -1100, -1101, -1102, -9000]
        self.assertTrue(is_monotonic(array))
