import unittest

from Days.Day7 import is_command, is_directory, is_file


class TestIsCommand(unittest.TestCase):
    def setUp(self) -> None:
        self.cmd = '$ cd'

    def test_returns_bool(self):
        self.assertIsInstance(
            is_command(''),
            bool
        )

    def test_is_not_a_command(self):
        self.assertFalse(
            is_command('')
        )

    def test_cd_command_single_char_dir(self):
        cd_cmd = f'{self.cmd} /'

        self.assertTrue(
            is_command(cd_cmd),
            f'"{cd_cmd}" is a command'
        )

    def test_cd_command_multi_char_dir(self):
        cd_cmd = f'{self.cmd} abcd'

        self.assertTrue(
            is_command(cd_cmd),
            f'"{cd_cmd}" is a command'
        )

    def test_ls_command(self):
        self.assertTrue(
            is_command('$ ls'),
            '"$ ls" is a command'
        )

    def test_invalid_command_starts_with_dollar_sign(self):
        self.assertFalse(
            is_command('$ abcd'),
            '"$ abcd" is not a command'
        )


class TestIsDirectory(unittest.TestCase):
    def test_returns_bool(self):
        self.assertIsInstance(
            is_directory(''),
            bool
        )

    def test_dir_valid(self):
        dir_name = 'a'

        self.assertTrue(
            is_directory(f'dir {dir_name}'),
            f'"{dir_name}" is a valid directory'
        )

    def test_invalid_dir(self):
        dir_name = '0'

        self.assertFalse(
            is_directory(f'dir {dir_name}'),
            f'"{dir_name}" is not a valid directory'
        )

    def test_space_in_dir_name(self):
        dir_name = 'a b'

        self.assertFalse(
            is_directory(f'dir {dir_name}'),
            f'"{dir_name}" is not a valid directory'
        )

    def test_main_dir(self):
        self.assertTrue(
            is_directory('dir /'),
            '"/" is a valid directory'
        )


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
