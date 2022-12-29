import unittest

from src import is_unique, first_unique_characters


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
            first_unique_characters('abcd'),
            int
        )

    def test_returns_4(self):
        self.assertEqual(
            first_unique_characters('abcd'),
            4,
            '"abcd" should be 4'
        )

    def test_returns_5(self):
        self.assertEqual(
            first_unique_characters('aabcd'),
            5,
            '"aabcd" should be 5'
        )

    def test_string_not_unique(self):
        with self.assertRaises(ValueError):
            first_unique_characters('aaaa')

    def test_string_shorter_than_window(self):
        with self.assertRaises(ValueError):
            first_unique_characters('')


if __name__ == '__main__':
    unittest.main()
