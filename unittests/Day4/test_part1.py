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


class TestTotalOverlappingPairs(unittest.TestCase):
    def setUp(self) -> None:
        self.one_overlap = CampCleanup(['2-5,3-3', '1-3,4-7'])
        self.no_overlap = CampCleanup(['2-5,1-2', '1-3,4-7'])
        self.two_overlap = CampCleanup(['2-5,3-3', '1-3,1-7'])

    def test_returns_int(self):
        self.assertIsInstance(
            self.one_overlap.total_overlapping_pairs(),
            int,
            'Should return integer'
        )

    def test_returns_one(self):
        self.assertEqual(
            self.one_overlap.total_overlapping_pairs(),
            1,
            'Should be 1'
        )

    def test_returns_two(self):
        self.assertEqual(
            self.two_overlap.total_overlapping_pairs(),
            2,
            'Should be 2'
        )
