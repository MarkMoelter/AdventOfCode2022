import unittest

from Day3.part1 import Part1


class TestSplitRucksack(unittest.TestCase):
    def setUp(self) -> None:
        self.rucksacks = ['ABCD', 'EFGH', 'HIJK', 'LMNO']
        self.p1 = Part1(self.rucksacks)

    def test_return_list(self):
        self.assertEqual(
            type(self.p1.split_rucksack()),
            list
        )

    def test_return_list_of_tuple(self):
        for ele in self.p1.split_rucksack():
            self.assertEqual(
                type(ele),
                tuple
            )

    def test_return_list_of_tuple_of_two_string(self):
        for ele in self.p1.split_rucksack()[0]:
            self.assertEqual(
                type(ele),
                str
            )

    def test_separate_in_half(self):
        split_rucksacks = Part1(['ABCD', 'EFGH']).split_rucksack()
        pocket_1, pocket_2 = split_rucksacks[-1]
        self.assertEqual(
            len(pocket_1),
            len(pocket_2)
        )


class TestCheckPockets(unittest.TestCase):
    def test_return_list(self):
        self.assertEqual(
            type(Part1().check_pockets('', '')),
            set
        )

    def test_values_in_list_return_string(self):
        for ele in Part1().check_pockets('', ''):
            self.assertEqual(
                type(ele),
                str
            )

    def test_raise_value_error_when_not_same_length(self):
        self.assertRaises(
            ValueError,
            Part1().check_pockets,
            pocket_1='fo',
            pocket_2='bar'
        )

    def test_return_A(self):
        self.assertEqual(
            Part1().check_pockets('AB', 'CA'),
            {'A'}
        )

    def test_return_A_and_B(self):
        self.assertEqual(
            Part1().check_pockets('ABC', 'GBA'),
            {'A', 'B'}
        )
        self.assertEqual(
            Part1().check_pockets('ABC', 'GBA'),
            {'B', 'A'}
        )


class TestAssignPriority(unittest.TestCase):
    def test_return_list(self):
        self.assertEqual(
            type(Part1().assign_priority('a')),
            int
        )

    def test_a_returns_one(self):
        self.assertEqual(
            Part1().assign_priority('a'),
            1
        )

    def test_z_returns_26(self):
        self.assertEqual(
            Part1().assign_priority('z'),
            26
        )

    def test_A_returns_27(self):
        self.assertEqual(
            Part1().assign_priority('A'),
            27
        )

    def test_Z_returns_52(self):
        self.assertEqual(
            Part1().assign_priority('Z'),
            52
        )

    def test_string_len_2_raises_TypeError(self):
        self.assertRaises(
            TypeError,
            Part1().assign_priority,
            'foo'
        )

    def test_numerical_value_raises_TypeError(self):
        self.assertRaises(
            TypeError,
            Part1().assign_priority,
            '0'
        )
