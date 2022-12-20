import unittest

from Days.Day5 import Command, ShippingYard


class TestMoveCrates(unittest.TestCase):
    def setUp(self) -> None:
        self.yard = ShippingYard()

    def test_returns_None(self):
        self.assertIsInstance(
            self.yard.move_crates(Command(1, 2, 3)),
        )

    def test_returns_command_object(self):
        pass
