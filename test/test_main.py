import pytest

from app import main as uut

'''
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
'''


def test_main():
    uut.main()