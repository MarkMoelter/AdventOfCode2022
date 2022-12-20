import unittest

from Days.Day4 import PartialOverlap


class TestOverlapScore(unittest.TestCase):
    def setUp(self) -> None:
        self.zero_overlap = PartialOverlap(['3-5,1-2', '1-3,4-7'])
        self.one_overlap = PartialOverlap(['2-5,3-3', '1-3,4-7'])
        self.two_overlap = PartialOverlap(['2-5,5-6', '1-3,3-7'])

    def test_returns_int(self):
        self.assertIsInstance(
            self.one_overlap.overlap_score(),
            int,
            'Should return an int'
        )

    def test_returns_zero(self):
        self.assertEqual(
            self.zero_overlap.overlap_score(),
            0,
            'Should be 0'
        )

    def test_returns_one(self):
        self.assertEqual(
            self.one_overlap.overlap_score(),
            1,
            'Should be 1'
        )

    def test_returns_two(self):
        self.assertEqual(
            self.two_overlap.overlap_score(),
            2,
            'Should be 2'
        )
