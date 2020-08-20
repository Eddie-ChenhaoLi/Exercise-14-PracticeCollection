import unittest
from practice01 import  add

class TestDemo(unittest.TestCase):

    def test_cal(self):
        assert add(1, 2) == 3