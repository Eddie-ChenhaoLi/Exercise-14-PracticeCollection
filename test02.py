import unittest
from practice02 import subtract


class TestDemo(unittest.TestCase):

    def test_cal(self):
        assert subtract(2, 1) == 0
