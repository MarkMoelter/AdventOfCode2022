import unittest

from Days.Day6 import is_unique, sliding_window


class TestIsUnique(unittest.TestCase):
    def test_returns_bool(self):
        self.assertIsInstance(
            is_unique('a'),
            bool,
            'Should be boolean'
        )

    def test_returns_true(self):
        self.assertTrue(
            is_unique('a', 'b', 'c')
        )

        self.assertTrue(
            is_unique('a')
        )

        self.assertTrue(
            is_unique('')
        )

    def test_returns_false(self):
        self.assertFalse(
            is_unique('a', 'a')
        )

        self.assertFalse(
            is_unique('A', 'A', 'b', 'c', '7')
        )


class TestSlidingWindow(unittest.TestCase):
    def test_returns_int(self):
        self.assertIsInstance(
            sliding_window('abcd'),
            int
        )

    def test_returns_3(self):
        self.assertEqual(
            sliding_window('abcd'),
            3,
            'Should be 3'
        )

    def test_returns_4(self):
        self.assertEqual(
            sliding_window('aabcd'),
            4,
            'Should be 4'
        )


if __name__ == '__main__':
    unittest.main()
