import unittest
import sys

sys.path.insert(0, '..')
from src.Float import Float
from src.bitstring import bitstring

class Constructors(unittest.TestCase) :
    def setUp(self) : 
        self.f = Float(1, length=32)

    def test_new(self) : 
        Float.__new__(Float, num=0, length=32)
        Float.__new__(Float, num=0.1, length=64)
        self.assertRaises(bitstring.CreationError, Float.__new__, Float, num='string', length=32)
        self.assertRaises(bitstring.CreationError, Float.__new__, Float, num=0, length=1)

    def test_init(self) : 
        self.assertAlmostEqual(self.f.float, 1)
        self.assertEqual(self.f.bin, '0_01111111_.00000000.00000000.0000000')

class SettersTestCase(unittest.TestCase) :
    def setUp(self) :
        self.f = Float(1.0000, length=64)

    def testSetFloat(self) : 
        self.f.float = 10
        self.f.float = 1.02

        def setFloat(value) : 
            self.f.float = value

        self.assertRaises(bitstring.CreationError, setFloat, 's')
        self.assertRaises(bitstring.CreationError, setFloat, [])

    def testSetBin(self) : 
        self.f.bin = '10000000000000000000000000000000'
        assertAlmostEqual(self.f.float = 0)
        self.f.bin = '1000000000000000000000000000000010000000000000000000000000000000'

        def setBin(value) : 
            self.f.bin = value

        self.assertRaises(bitstring.CreationError, setBin, 1)
        self.assertRaises(bitstring.CreationError, setBin, 2.334)
        self.assertRaises(bitstring.CreationError, setBin, 'sllkjdfkkjdklllllllllllkkjlkjlll')

class GettersTestCase(unittest.TestCase) : 
    def setUp(self) : 
        self.f = Float(10, length=64)

    def testGetFloat(self) : 
        self.f.float = 1
        assertAlmostEqual(self.f.float, 10)
        assertEqual()

if __name__ == '__main__' : 
    unittest.main()