import unittest
import random

from permutations import permutations
from itertools import permutations as itertools_permutations


class TestPermutations(unittest.TestCase):
    def test_itertools_permutations(self):
        for tc in range(10):
            lst = random.choices(range(1_000), k=random.randint(3, 8))
            with self.subTest(lst=lst):
                our_result = set(tuple(i) for i in permutations(lst))
                there_result = set(itertools_permutations(lst))
                self.assertEqual(our_result, there_result)


if __name__ == "__main__":
    unittest.main()
