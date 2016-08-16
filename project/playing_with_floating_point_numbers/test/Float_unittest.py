import unittest
import sys
import math
import utils

sys.path.insert(0, '..')
from src.Float import Float
from src.bitstring import bitstring

class Constructors(unittest.TestCase) :

	def testCreationFromFloat(self) : 

		def float32_assertionAlmostEqual(testValue, f) : 
			def mod(x) : 
				if x < 0 : 
					return -x
				return x

			error = mod((testValue - f.float)*(10**4))
			return error < 1

		f = Float(4.52344)
		self.assertEqual(float32_assertionAlmostEqual(4.52344, f), True) 

		f = Float(4.52344, length=32)
		bin = '01000000100100001100000000000101'		
		self.assertEqual(float32_assertionAlmostEqual(4.52344, f), True)
		self.assertEqual(f.bin, bin)

		f = Float(4.52344, length=64)
		bin = '0100000000010010000110000000000010100111110001011010110001000111'
		self.assertEqual(f.float, 4.52344)
		self.assertEqual(f.bin, bin)

		f = Float(-2.33, length=64)
		bin = '1100000000000010101000111101011100001010001111010111000010100100'
		self.assertEqual(f.float, -2.33)
		self.assertEqual(f.bin, bin)

		# +-0
		f = Float(-0.00, length=64)
		bin = '1000000000000000000000000000000000000000000000000000000000000000'
		self.assertEqual(f.float, -0.00)
		self.assertNotEqual(f.bin, Float(+0.00).bin)
		self.assertEqual(f.bin, bin)

		f = Float(+0.00, length=64)
		bin = '0000000000000000000000000000000000000000000000000000000000000000'
		self.assertEqual(f.float, +0.00)
		self.assertNotEqual(f.bin, Float(-0.00).bin)
		self.assertEqual(f.bin, bin)

		# +-inf
		f = Float(-float('inf'), length=64)
		bin = '1111111111110000000000000000000000000000000000000000000000000000'
		self.assertEqual(f.float, -float('inf'))
		self.assertNotEqual(f.float, float('inf'))
		self.assertEqual(f.bin, bin)

		f = Float(float('inf'), length=64)
		bin = '0111111111110000000000000000000000000000000000000000000000000000'	
		self.assertEqual(f.float, float('inf'))
		self.assertNotEqual(f.float, -float('inf'))
		self.assertEqual(f.bin, bin)

		# NaN
		f = Float(float('nan'), length=64)
		self.assertEqual(math.isnan(f.float), True)

		# integer argument
		f = Float(10)
		self.assertAlmostEqual(f.float, 10.000)
		self.assertEqual(f.bin, Float(10.00).bin)

	def testCreateFromBin(self) : 

		def float32_assertionAlmostEqual(testValue, f) : 
			def mod(x) : 
				if x < 0 : 
					return -x
				return x

			error = mod((testValue - f.float)*(10**4))
			return error < 1

		bin = '01000000100100001100000000000101'		
		f = Float(bin)
		self.assertEqual(float32_assertionAlmostEqual(4.52344, f), True) 
		self.assertEqual(f.bin, bin)

		bin = '01000000100100001100000000000101'		
		f = Float(bin)
		self.assertEqual(float32_assertionAlmostEqual(4.52344, f), True)
		self.assertEqual(f.bin, bin)

		bin = '0100000000010010000110000000000010100111110001011010110001000111'
		f = Float(bin, length=64)
		self.assertEqual(f.float, 4.52344)
		self.assertEqual(f.bin, bin)

		bin = '1100000000000010101000111101011100001010001111010111000010100100'
		f = Float(bin, length=64)
		self.assertEqual(f.float, -2.33)
		self.assertEqual(f.bin, bin)

		# +-0
		bin = '1000000000000000000000000000000000000000000000000000000000000000'
		f = Float(bin, length=64)
		self.assertEqual(f.float, -0.00)
		self.assertNotEqual(f.bin, Float(+0.00).bin)
		self.assertEqual(f.bin, bin)

		bin = '0000000000000000000000000000000000000000000000000000000000000000'
		f = Float(bin, length=64)
		self.assertEqual(f.float, +0.00)
		self.assertNotEqual(f.bin, Float(-0.00).bin)
		self.assertEqual(f.bin, bin)

		# +-inf
		bin = '1111111111110000000000000000000000000000000000000000000000000000'
		f = Float(bin, length=64)
		self.assertEqual(f.float, -float('inf'))
		self.assertNotEqual(f.float, float('inf'))
		self.assertEqual(f.bin, bin)

		bin = '0111111111110000000000000000000000000000000000000000000000000000'	
		f = Float(bin, length=64)
		self.assertEqual(f.float, float('inf'))
		self.assertNotEqual(f.float, -float('inf'))
		self.assertEqual(f.bin, bin)

		# NaN
		bin = '0111111111111000000000000000000000000000000000000000000000000000'
		f = Float(bin, length=64)
		self.assertEqual(math.isnan(f.float), True)

	def testCreationErrors(self) : 
		self.assertRaises(bitstring.CreationError, Float, num=0, length=10)
		self.assertRaises(bitstring.CreationError, Float, num='0100')
		self.assertRaises(bitstring.CreationError, Float, num='0111111111110000000000000000000000000000000000000000000000000000')
		Float(num='0111111111110000000000000000000000000000000000000000000000000000', length=64)
		self.assertRaises(bitstring.CreationError, Float, num='0111111111110000000000000001450000008000000000000000000000000000', length=64)
		self.assertRaises(bitstring.CreationError, Float, num=[])

class Properties(unittest.TestCase) :

	def testFloat(self) : 

		def float32_assertionAlmostEqual(testValue, f) : 
			def mod(x) : 
				if x < 0 : 
					return -x
				return x

			error = mod((testValue - f.float)*(10**4))
			return error < 1

		f = Float(0, length=32)
		f.float = 4.52344
		bin = '01000000100100001100000000000101'		
		self.assertEqual(float32_assertionAlmostEqual(4.52344, f), True)
		self.assertEqual(f.bin, bin)

		f = Float(0, length=64)
		f.float = 4.52344
		bin = '0100000000010010000110000000000010100111110001011010110001000111'
		self.assertEqual(f.float, 4.52344)
		self.assertEqual(f.bin, bin)

		f.float = -2.33
		bin = '1100000000000010101000111101011100001010001111010111000010100100'
		self.assertEqual(f.float, -2.33)
		self.assertEqual(f.bin, bin)

		# +-0
		f.float = -0.00
		bin = '1000000000000000000000000000000000000000000000000000000000000000'
		self.assertEqual(f.float, -0.00)
		self.assertNotEqual(f.bin, Float(+0.00).bin)
		self.assertEqual(f.bin, bin)

		f.float = +0.00
		bin = '0000000000000000000000000000000000000000000000000000000000000000'
		self.assertEqual(f.float, +0.00)
		self.assertNotEqual(f.bin, Float(-0.00).bin)
		self.assertEqual(f.bin, bin)

		# +-inf
		f.float = -float('inf')
		bin = '1111111111110000000000000000000000000000000000000000000000000000'
		self.assertEqual(f.float, -float('inf'))
		self.assertNotEqual(f.float, float('inf'))
		self.assertEqual(f.bin, bin)

		f.float = float('inf')
		bin = '0111111111110000000000000000000000000000000000000000000000000000'	
		self.assertEqual(f.float, float('inf'))
		self.assertNotEqual(f.float, -float('inf'))
		self.assertEqual(f.bin, bin)

		# NaN
		f.float = float('nan')
		self.assertEqual(math.isnan(f.float), True)

		# integer argument
		f.float = 10
		self.assertAlmostEqual(f.float, 10.000)
		self.assertEqual(f.bin, Float(10.00, length=64).bin)

		def setFloat(f, value) : 
			f.float = value

		#
		self.assertRaises(bitstring.CreationError, setFloat, f, 's')
		self.assertRaises(bitstring.CreationError, setFloat, f, '0111111111110000000000000000000000000000000000000000000000000000')

	def testBin(self) : 
		def float32_assertionAlmostEqual(testValue, f) : 
			def mod(x) : 
				if x < 0 : 
					return -x
				return x

			error = mod((testValue - f.float)*(10**4))
			return error < 1

		f = Float(0, length=32)
		bin = '01000000100100001100000000000101'		
		f.bin = bin
		self.assertEqual(float32_assertionAlmostEqual(4.52344, f), True)
		self.assertEqual(f.bin, bin)

		f = Float(0, length=64)
		bin = '0100000000010010000110000000000010100111110001011010110001000111'
		f.bin = bin
		self.assertEqual(f.float, 4.52344)
		self.assertEqual(f.bin, bin)

		bin = '1100000000000010101000111101011100001010001111010111000010100100'
		f.bin = bin
		self.assertEqual(f.float, -2.33)
		self.assertEqual(f.bin, bin)

		# +-0
		bin = '1000000000000000000000000000000000000000000000000000000000000000'
		f.bin = bin
		self.assertEqual(f.float, -0.00)
		self.assertNotEqual(f.bin, Float(+0.00).bin)
		self.assertEqual(f.bin, bin)

		bin = '0000000000000000000000000000000000000000000000000000000000000000'
		f.bin = bin
		self.assertEqual(f.float, +0.00)
		self.assertNotEqual(f.bin, Float(-0.00).bin)
		self.assertEqual(f.bin, bin)

		# +-inf
		bin = '1111111111110000000000000000000000000000000000000000000000000000'
		f.bin = bin
		self.assertEqual(f.float, -float('inf'))
		self.assertNotEqual(f.float, float('inf'))
		self.assertEqual(f.bin, bin)

		bin = '0111111111110000000000000000000000000000000000000000000000000000'	
		f.bin = bin
		self.assertEqual(f.float, float('inf'))
		self.assertNotEqual(f.float, -float('inf'))
		self.assertEqual(f.bin, bin)

		def setBin(f, value) : 
			f.bin = value

		# Error
		self.assertRaises(bitstring.CreationError, setBin, f, 's')
		self.assertRaises(bitstring.CreationError, setBin, f, 10.03)
		self.assertRaises(bitstring.CreationError, setBin, f, '01111111111100000000000000000000')

	def test_Mantissa_Exponent_Sign_getters(self) : 

		def float32_assertionAlmostEqual(testValue, f) : 
			def mod(x) : 
				if x < 0 : 
					return -x
				return x

			error = mod((testValue - f.float)*(10**4))
			return error < 1

		f32 = Float(0, length=32)
		f64 = Float(0, length=64)

		# positive
		bin = '01000110000110110100100101100001'
		f32.bin = bin
		self.assertEqual(f32.bin, bin)
		self.assertEqual(f32.raw_sign, '0')
		self.assertEqual(f32.raw_exponent, '10001100')
		self.assertEqual(f32.raw_mantissa, '00110110100100101100001')

		bin = '0100000000010010000110000000000010100111110001011010110001000111'
		f64.bin = bin
		self.assertEqual(f64.bin, bin)
		self.assertEqual(f64.raw_sign, '0')
		self.assertEqual(f64.raw_exponent, '10000000001')
		self.assertEqual(f64.raw_mantissa, '0010000110000000000010100111110001011010110001000111')

		# negative
		bin = '11001011001010011010110101000010'
		f32.bin = bin
		self.assertEqual(f32.bin, bin)
		self.assertEqual(f32.raw_sign, '1')
		self.assertEqual(f32.raw_exponent, '10010110')
		self.assertEqual(f32.raw_mantissa, '01010011010110101000010')

		bin = '1100000000000010101000111101011100001010001111010111000010100100'
		f64.bin = bin
		self.assertEqual(f64.bin, bin)
		self.assertEqual(f64.raw_sign, '1')
		self.assertEqual(f64.raw_exponent, '10000000000')
		self.assertEqual(f64.raw_mantissa, '0010101000111101011100001010001111010111000010100100')

		# +-0
		bin = '00000000000000000000000000000000'
		f32.bin = bin
		self.assertEqual(f32.bin, bin)
		self.assertEqual(f32.raw_sign, '0')
		self.assertEqual(f32.raw_exponent, '00000000')
		self.assertEqual(f32.raw_mantissa, '00000000000000000000000')

		bin = '1000000000000000000000000000000000000000000000000000000000000000'
		f64.bin = bin
		self.assertEqual(f64.bin, bin)
		self.assertEqual(f64.raw_sign, '1')
		self.assertEqual(f64.raw_exponent, '00000000000')
		self.assertEqual(f64.raw_mantissa, '0000000000000000000000000000000000000000000000000000')

		bin = '10000000000000000000000000000000'
		f32.bin = bin
		self.assertEqual(f32.bin, bin)
		self.assertEqual(f32.raw_sign, '1')
		self.assertEqual(f32.raw_exponent, '00000000')
		self.assertEqual(f32.raw_mantissa, '00000000000000000000000')

		bin = '0000000000000000000000000000000000000000000000000000000000000000'
		f64.bin = bin
		self.assertEqual(f64.bin, bin)
		self.assertEqual(f64.raw_sign, '0')
		self.assertEqual(f64.raw_exponent, '00000000000')
		self.assertEqual(f64.raw_mantissa, '0000000000000000000000000000000000000000000000000000')

		# +-inf
		bin = '01111111100000000000000000000000'
		f32.bin = bin
		self.assertEqual(f32.bin, bin)
		self.assertEqual(f32.raw_sign, '0')
		self.assertEqual(f32.raw_exponent, '11111111')
		self.assertEqual(f32.raw_mantissa, '00000000000000000000000')
		bin = '1111111111110000000000000000000000000000000000000000000000000000'

		f64.bin = bin
		self.assertEqual(f64.bin, bin)
		self.assertEqual(f64.raw_sign, '1')
		self.assertEqual(f64.raw_exponent, '11111111111')
		self.assertEqual(f64.raw_mantissa, '0000000000000000000000000000000000000000000000000000')

		bin = '11111111100000000000000000000000'
		f32.bin = bin
		self.assertEqual(f32.bin, bin)
		self.assertEqual(f32.raw_sign, '1')
		self.assertEqual(f32.raw_exponent, '11111111')
		self.assertEqual(f32.raw_mantissa, '00000000000000000000000')

		bin = '0111111111110000000000000000000000000000000000000000000000000000'	
		f64.bin = bin
		self.assertEqual(f64.bin, bin)
		self.assertEqual(f64.raw_sign, '0')
		self.assertEqual(f64.raw_exponent, '11111111111')
		self.assertEqual(f64.raw_mantissa, '0000000000000000000000000000000000000000000000000000')

		# NaN
		bin = '01111111101111111011111111111111'
		f32.bin = bin
		self.assertEqual(f32.bin, bin)
		self.assertEqual(f32.raw_exponent, '11111111')
		self.assertNotEqual(f32.raw_mantissa, '00000000000000000000000')

		bin = '0111111111110000000010000000000000000000000000000000000000000000'	
		f64.float = float('nan')
		self.assertEqual(math.isnan(f64.float), True)
		self.assertEqual(f64.raw_exponent, '11111111111')
		self.assertNotEqual(f64.raw_mantissa, '0000000000000000000000000000000000000000000000000000')

	def test_ExponentField_ExponentValue(self) : 
		f = Float()
		f.raw_exponent = '10000001'
		self.assertEqual(f.raw_exponent, '10000001')
		self.assertEqual(f.exponent_field, 129)
		self.assertEqual(f.exponent_value, 2)
		f.raw_exponent = '11111111'
		self.assertEqual(f.raw_exponent, '11111111')
		self.assertEqual(f.exponent_field, 255)
		self.assertEqual(f.exponent_value, 128)

		f = Float(length=64)
		f.raw_exponent = '10000000000'
		self.assertEqual(f.raw_exponent, '10000000000')
		self.assertEqual(f.exponent_field, 1024)
		self.assertEqual(f.exponent_value, 1)
		f.raw_exponent = '11111111111'
		self.assertEqual(f.raw_exponent, '11111111111')
		self.assertEqual(f.exponent_field, 2047)
		self.assertEqual(f.exponent_value, 1024)

	def testMantissaSetter(self) : 
		
		f32 = Float()
		f64 = Float(length=64)
		def setMantissa(f, value) : 
			f.raw_mantissa = value

		bin = '01000110000110110100100101100001'
		f32.bin = bin
		self.assertEqual(f32.bin, bin)
		self.assertEqual(f32.raw_sign, '0')
		self.assertEqual(f32.raw_exponent, '10001100')
		self.assertEqual(f32.raw_mantissa, '00110110100100101100001')
		# length 23
		f32.raw_mantissa = '10000000000000000000000'
		self.assertEqual(f32.raw_mantissa, '10000000000000000000000')
		# length 24	
		self.assertRaises(bitstring.CreationError, setMantissa, f32, '100000000000000000000000')
		# exponent and sign (should remain unchanged)
		self.assertEqual(f32.raw_sign, '0')
		self.assertEqual(f32.raw_exponent, '10001100')
		# invalid binary
		self.assertRaises(bitstring.CreationError, setMantissa, f32, '10000000000000030000000')
		# invalid type
		self.assertRaises(bitstring.CreationError, setMantissa, f32, 398.4)

		bin = '0100000000010010000110000000000010100111110001011010110001000111'
		f64.bin = bin
		self.assertEqual(f64.bin, bin)
		self.assertEqual(f64.raw_sign, '0')
		self.assertEqual(f64.raw_exponent, '10000000001')
		self.assertEqual(f64.raw_mantissa, '0010000110000000000010100111110001011010110001000111')
		# length 52 
		f64.raw_mantissa = '1010101010000000000011111111110101010101000000000011'
		self.assertEqual(f64.raw_mantissa, '1010101010000000000011111111110101010101000000000011')
		# length 50
		self.assertRaises(bitstring.CreationError, setMantissa, f64, '10101010100000000000111111111101010101010000000001')
		# exponent and sign (should remain unchanged)
		self.assertEqual(f64.raw_sign, '0')
		self.assertEqual(f64.raw_exponent, '10000000001')
		# invalid binary
		self.assertRaises(bitstring.CreationError, setMantissa, f64, '1010101010000000000011111111110101010101000000000013')
		# invalid type
		self.assertRaises(bitstring.CreationError, setMantissa, f64, 398.4)	

	def testExponentSetter(self) : 
		f32 = Float()
		f64 = Float(length=64)
		def setExponent(f, value) : 
			f.raw_exponent = value

		bin = '01000110000110110100100101100001'
		f32.bin = bin
		self.assertEqual(f32.bin, bin)
		self.assertEqual(f32.raw_sign, '0')
		self.assertEqual(f32.raw_exponent, '10001100')
		self.assertEqual(f32.raw_mantissa, '00110110100100101100001')
		# length 8
		f32.raw_exponent = '10101010'
		# length 11	
		self.assertRaises(bitstring.CreationError, setExponent, f32, '10111111111')
		# exponent and sign (should remain unchanged)
		self.assertEqual(f32.raw_sign, '0')
		self.assertEqual(f32.raw_mantissa, '00110110100100101100001')
		# invalid binary
		self.assertRaises(bitstring.CreationError, setExponent, f32, '10000003')
		# invalid type
		self.assertRaises(bitstring.CreationError, setExponent, f32, {})

		bin = '0100000000010010000110000000000010100111110001011010110001000111'
		f64.bin = bin
		self.assertEqual(f64.bin, bin)
		self.assertEqual(f64.raw_sign, '0')
		self.assertEqual(f64.raw_exponent, '10000000001')
		self.assertEqual(f64.raw_mantissa, '0010000110000000000010100111110001011010110001000111')
		# length 11
		f64.raw_exponent = '10101010001'
		self.assertEqual(f64.raw_exponent, '10101010001')
		# length 50
		self.assertRaises(bitstring.CreationError, setExponent, f64, '10001010')
		# exponent and sign (should remain unchanged)
		self.assertEqual(f64.raw_sign, '0')
		self.assertEqual(f64.raw_mantissa,'0010000110000000000010100111110001011010110001000111') 
		# invalid binary
		self.assertRaises(bitstring.CreationError, setExponent, f64, '10111000009')
		# invalid type
		self.assertRaises(bitstring.CreationError, setExponent, f64, [])

	def testSignSetter(self) : 
		f32 = Float()
		f64 = Float(length=64)
		def setSign(f, value) : 
			f.raw_sign = value

		bin = '01000110000110110100100101100001'
		f32.bin = bin
		self.assertEqual(f32.bin, bin)
		self.assertEqual(f32.raw_sign, '0')
		self.assertEqual(f32.raw_exponent, '10001100')
		self.assertEqual(f32.raw_mantissa, '00110110100100101100001')
		# length 1
		f32.raw_sign = '1'
		self.assertEqual(f32.raw_sign, '1')
		# length 0	
		self.assertRaises(bitstring.CreationError, setSign, f32, '')
		# exponent and sign (should remain unchanged)
		self.assertEqual(f32.raw_exponent, '10001100')
		self.assertEqual(f32.raw_mantissa, '00110110100100101100001')
		# invalid binary
		self.assertRaises(bitstring.CreationError, setSign, f32, '3')
		# invalid type
		self.assertRaises(bitstring.CreationError, setSign, f32, {})

if __name__ == '__main__' : 
	suiteList = ['Constructors', 'Properties']
	utils.runSuites(suiteList)

	