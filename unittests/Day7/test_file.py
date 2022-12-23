import unittest

from Days.Day7 import is_file


class TestIsFile(unittest.TestCase):
    def test_return_bool(self):
        self.assertIsInstance(
            is_file(''),
            bool
        )

    def test_file_valid_wo_ext(self):
        filename = '123 abs'
        self.assertTrue(
            is_file(filename),
            f'"{filename}" is a valid file'
        )

    def test_valid_w_ext(self):
        filename = '232 log.log'
        self.assertTrue(
            is_file(filename),
            f'"{filename}" is a valid file'
        )

    def test_invalid_ext(self):
        filename = '1 abd.sd'
        self.assertFalse(
            is_file(filename),
            f'"{filename}" is not a valid file'
        )

    def test_invalid_name(self):
        filename = '10378 7.asd'
        self.assertFalse(
            is_file(filename),
            f'"{filename}" is not a valid file'
        )

    def test_neg_size(self):
        filename = '-123 adg'
        self.assertFalse(
            is_file(filename),
            f'"{filename}" is not a valid file'
        )

    def test_size_0(self):
        filename = '0 gie.sdf'
        self.assertFalse(
            is_file(filename),
            f'"{filename}" is not a valid file size'
        )

    def test_valid_with_0_in_size(self):
        filename = '1201 tot.exc'
        self.assertTrue(
            is_file(filename),
            f'"{filename}" is a valid file size'
        )

    def test_leading_0_in_size(self):
        filename = '0000000430 abcd'
        self.assertTrue(
            is_file(filename),
            f'"{filename}" is a valid file size'
        )


if __name__ == '__main__':
    unittest.main()
