from unittest import TestCase

from algo_questions.arrays.longest_peak import get_longest_peak


class LongestPeakTests(TestCase):
    def test_get_longest_peak(self):
        self.assertEqual(get_longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]), 6)
        self.assertEqual(get_longest_peak([1, 2, 3]), 0)
        self.assertEqual(get_longest_peak([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]), 11)
        self.assertEqual(get_longest_peak([1, 4, 3]), 3)
