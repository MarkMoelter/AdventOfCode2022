import unittest

from Days.Day7 import create_file_system, File


class TestCreateFileSystem(unittest.TestCase):
    def setUp(self) -> None:
        self.empty_input = []
        self.single_file = ['1 abc.log']
        self.invalid_file = ['12 7']

    def test_returns_file(self):
        self.assertIsInstance(
            create_file_system(self.empty_input),
            File
        )

    def test_root_has_files(self):
        self.assertTrue(
            create_file_system(self.single_file).contents
        )

    def test_root_does_not_add_invalid(self):
        self.assertFalse(
            create_file_system(self.invalid_file).contents
        )


if __name__ == '__main__':
    unittest.main()
