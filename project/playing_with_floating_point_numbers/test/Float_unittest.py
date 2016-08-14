import unittest
import sys

sys.path.insert(0, '..')
from src.Float import Float

class SettersTestCase(unittest.TestCase) :
    def setUp(self) :
        self.f = Float(1.0000, length=64)

    def test_float_setter(self) : 
        self.failUnless(True)

if __name__ == '__main__' : 
    unittest.main()