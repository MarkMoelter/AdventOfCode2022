import unittest

from Day3 import Part2


class TestSplitIntoGroups(unittest.TestCase):
    def setUp(self) -> None:
        self.basic_ruck = ['abca', 'defd', 'ghig', 'jklj', 'xyzx', 'qweq']

    def test_returns_dict(self):
        self.assertEqual(
            type(Part2(self.basic_ruck).split_into_groups()),
            dict
        )

    def test_return_right_vals(self):
        self.assertEqual(
            Part2(self.basic_ruck).split_into_groups(),
            {0: ['abca', 'defd', 'ghig'],
             1: ['jklj', 'xyzx', 'qweq']
             }
        )


class TestGetDuplicate(unittest.TestCase):
    def setUp(self):
        self.basic_ruck = ['abc', 'defa', 'gahig']

    def test_returns_string(self):
        self.assertEqual(
            type(Part2().get_duplicate(self.basic_ruck)),
            str
        )

    def test_returns_a(self):
        self.assertEqual(
            Part2().get_duplicate(self.basic_ruck),
            'a'
        )

    def test_returns_A(self):
        self.assertEqual(
            Part2().get_duplicate(['ABa', 'HGA', 'POA']),
            'A'
        )

