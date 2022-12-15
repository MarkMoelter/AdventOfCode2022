import unittest

from Day5.command import Command
from Day5.main import parse_commands


class TestParseCommands(unittest.TestCase):
    def setUp(self) -> None:
        self.no_vals = parse_commands([''])

    def test_returns_list(self):
        self.assertIsInstance(
            self.no_vals,
            list
        )

    def test_returns_command_objects(self):
        self.assertIsInstance(
            self.no_vals[0],
            Command
        )

    def test_returns_command_1_3_5(self):
        self.assertEqual(
            parse_commands(['move 1 from 3 to 5']),
            Command(1, 3, 5)
        )


if __name__ == '__main__':
    unittest.main()
