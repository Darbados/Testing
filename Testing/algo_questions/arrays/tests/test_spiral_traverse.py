from unittest import TestCase

from algo_questions.arrays.spiral_traverse import spiral_traverse


class SpiralTraverseTests(TestCase):
    def test_empty_array(self):
        self.assertRaises(AssertionError, lambda: spiral_traverse([]))

    def test_single_row_array(self):
        self.assertEqual(spiral_traverse([[3, 5, 4, 8, 10]]), [3, 5, 4, 8, 10])

    def test_two_row_array(self):
        self.assertEqual(
            spiral_traverse(
                [[3, 5, 4, 8, 10], [6, 7, 11, 12, 16]],
            ),
            [3, 5, 4, 8, 10, 16, 12, 11, 7, 6],
        )

    def test_n_row_array(self):
        self.assertEqual(
            spiral_traverse([
                [2, 3, 4, 8],
                [4, 5, 6, 7],
                [10, 11, 9, 3],
            ]),
            [2, 3, 4, 8, 7, 3, 9, 11, 10, 4, 5, 6]
        )
