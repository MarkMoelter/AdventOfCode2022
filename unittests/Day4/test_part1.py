import unittest

from Day4 import CampCleanup


class TestProcessInput(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_returns_list(self):
        self.assertIsInstance(
            CampCleanup().process_input(),
            list
        )
