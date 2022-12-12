import unittest

from Day3.part2 import Part2

class TestSplitGroupsThree(unittest.TestCase):
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
            {0: [('ab', 'ca'), ('de', 'fd'), ('gh', 'ig')],
             1: [('jk', 'lj'), ('xy', 'zx'), ('qw', 'eq')]
             }
        )
