import unittest


class MyTestClass(unittest.TestCase):
    def test_something(self):
        self.assertEqual('', '')


if __name__ == '__main__':
    unittest.main()
