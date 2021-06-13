from unittest import TestCase

from algo_questions.arrays.array_of_products import get_array_of_products


class ArrayOfProductsTests(TestCase):
    def test_array_of_products(self):
        self.assertEqual(get_array_of_products([1, 1, 1, 1]), [1, 1, 1, 1])
        self.assertEqual(get_array_of_products([5, 1, 4, 2]), [8, 40, 10, 20])
