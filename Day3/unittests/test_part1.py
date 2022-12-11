import unittest

from Day3.part1 import Part1


class TestSplitRucksack(unittest.TestCase):
    def test_returns_list_of_tuples_of_strings(self):
        self.assertEqual(
            type(Part1().split_rucksack()),
            list
        )

        for ele in Part1().split_rucksack():
            self.assertEqual(
                type(ele),
                tuple
            )

        for ele in Part1().split_rucksack()[0]:
            self.assertEqual(
                type(ele),
                str
            )

    def test_separate_in_half(self):
        split_rucksacks = Part1(['ABCD', 'EFGH']).split_rucksack()
        pocket1, pocket2 = split_rucksacks[-1]
        self.assertEqual(
            len(pocket1),
            len(pocket2)
        )