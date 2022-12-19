import unittest

from Day5 import Command, ParseInput


class TestParseCommands(unittest.TestCase):
    def setUp(self) -> None:
        input_ = ['asdak ', 'move 1 from 3 to 5', ' ']
        self.basic = ParseInput(input_).parse_commands()

    def test_returns_list(self):
        self.assertIsInstance(
            self.basic,
            list,
            'Should be list'
        )

    def test_returns_command_objects(self):
        self.assertIsInstance(
            self.basic[0],
            Command,
            'Should be a Command object'
        )

    def test_returns_command_1_3_5(self):
        self.assertEqual(
            self.basic,
            [Command(1, 3, 5)],
            'Should have values 1, 3, and 5'
        )


class TestColumnSetup(unittest.TestCase):
    def setUp(self) -> None:
        input_ = [
            '                    [L]     [H] [W]',
            '                [J] [Z] [J] [Q] [Q]',
            '[S]             [M] [C] [T] [F] [B]',
            '[P]     [H]     [B] [D] [G] [B] [P]',
            '[W]     [L] [D] [D] [J] [W] [T] [C]',
            '[N] [T] [R] [T] [T] [T] [M] [M] [G]',
            '[J] [S] [Q] [S] [Z] [W] [P] [G] [D]',
            '[Z] [G] [V] [V] [Q] [M] [L] [N] [R]',
            ' 1   2   3   4   5   6   7   8   9 '
        ]
        self.basic = ParseInput(input_).column_setup()

    def test_returns_dict(self):
        self.assertIsInstance(
            self.basic,
            dict,
            'Should be a dict'
        )

    def test_list_is_not_blank(self):
        for key, list_ in self.basic.items():
            self.assertTrue(
                list_,
                f'List with key: {key} should not be blank'
            )


if __name__ == '__main__':
    unittest.main()
