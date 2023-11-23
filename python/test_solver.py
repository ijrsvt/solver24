import unittest

from solver import solve


class TestConformance(unittest.TestCase):
    def test_examples(self):
        examples = [
            (6, 1, 3, 4),
            (3, 6, 6, 11),
            (3, 5, 7, 13),
            (2, 5, 5, 10),
            (2, 3, 5, 12),
            (12, 2, 1, 1),
            (8, 1, 1, 1),
        ]
        for example in examples:
            with self.subTest(example=example):
                result = solve(*example)
                self.assertGreater(len(result), 0)


if __name__ == "__main__":
    unittest.main()
