import unittest

from Day4 import CampCleanup


class TestProcessInput(unittest.TestCase):
    def setUp(self) -> None:
        self.test_obj = CampCleanup(['2-5,3-3', '1-3,4-7'])

    def test_returns_list(self):
        self.assertIsInstance(
            self.test_obj.process_input(),
            list,
            'Should return list'
        )

    def test_list_not_empty(self):
        self.assertTrue(
            self.test_obj.process_input(),
            'List should not be empty'
        )

    def test_returns_tuple(self):
        self.assertIsInstance(
            self.test_obj.process_input()[0],
            tuple,
            'Should return tuple'
        )

    def test_tuple_not_empty(self):
        self.assertTrue(
            self.test_obj.process_input()[0],
            'Tuple should not be empty'
        )

    def test_returns_set(self):
        self.assertIsInstance(
            self.test_obj.process_input()[0][0],
            set,
            'Should return set'
        )

    def test_set_not_empty(self):
        self.assertTrue(
            self.test_obj.process_input()[0][0],
            'Set should not be empty'
        )

    def test_returns_correct_output(self):
        self.assertEqual(
            self.test_obj.process_input(),
            [
                ({2, 3, 4, 5}, {3}),
                ({1, 2, 3}, {4, 5, 6, 7})
            ]
        )
