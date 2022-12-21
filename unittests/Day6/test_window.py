import unittest

from Days.Day6 import is_unique


class TestIsUnique(unittest.TestCase):
    def test_returns_bool(self):
        self.assertIsInstance(
            is_unique('a'),
            bool,
            'Should be boolean'
        )

    def test_returns_true(self):
        self.assertTrue(
            is_unique('a', 'b', 'c'),
            'Should be True'
        )

    def test_returns_false(self):
        self.assertFalse(
            is_unique('a', 'a'),
        )

        self.assertFalse(
            is_unique('A', 'A', 'b', 'c', '7')
        )


if __name__ == '__main__':
    unittest.main()
