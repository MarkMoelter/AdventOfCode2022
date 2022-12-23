import unittest

from Days.Day7 import File


class TestCalcSize(unittest.TestCase):
    def setUp(self) -> None:
        self.file = File('test', 100, False)

    def test_returns_int(self):
        self.assertIsInstance(
            self.file.calc_size(),
            int
        )


if __name__ == '__main__':
    unittest.main()
