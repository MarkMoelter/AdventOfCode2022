import unittest

from Days.Day7 import is_command


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


if __name__ == '__main__':
    unittest.main()
