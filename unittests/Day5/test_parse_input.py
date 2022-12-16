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
        input_ = ['asdak ', 'move 1 from 3 to 5', ' ']
        self.basic = ParseInput(input_).column_setup()


def test_returns_dict(self):
        self.assertIsInstance(
            self.basic,
            dict,
            'Should return a dict'
        )


if __name__ == '__main__':
    unittest.main()
