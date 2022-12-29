import unittest

from src.Day7 import create_file_system


class TestCreateFileSystem(unittest.TestCase):
    def setUp(self) -> None:
        self.empty_input = []
        self.single_file = ['1 abc.log']
        self.invalid_file = ['12 7']

    def test_returns_tuple(self):
        self.assertIsInstance(
            create_file_system(self.empty_input),
            tuple
        )


if __name__ == '__main__':
    unittest.main()
