import unittest
import sys
import utils
import random
from colour_runner.runner import ColourTextTestRunner

sys.path.insert(0, '..')
from src.Float import Float
from src.bitstring import bitstring
from src.IterativeLogarithmicMultiplier import IntegerIterativeLogarithmicMultiplier
from src.IterativeLogarithmicMultiplier import FloatingPointIterativeLogarithmicMultiplier

class TestIntegerIterativeLogarithmicMultiplier() : 
	
	class Constructor(unittest.TestCase) : 
		pass

	class Multiply(unittest.TestCase) : 
		
		def setUp(self) : 
			self.multiplier = IntegerIterativeLogarithmicMultiplier()

		def mod(self, num) : 
			if num < 0 : 
				return -num
			return num

		def testOperation(self) : 
			for i in range(100) : 
				n1 = random.randint(1, 100)
				n2 = random.randint(1, 100)
				result_reqd = n1*n2
				result_getd = self.multiplier.multiply(bin(n1)[2:], bin(n2)[2:], 5)
				self.assertEqual(self.multiplier.validateBinary(result_getd), True)
				relativeError = self.mod(result_reqd - int(result_getd, base=2))*1.0 / result_reqd
				print(str(n1) + ' * ' + str(n2) + ' -- ' + str(result_reqd) + ' / ' + str(int(result_getd, base=2)) + ' -- ' + str(relativeError))

	class P0_approx(unittest.TestCase) : 

		def setUp(self) : 
			self.multiplier = IntegerIterativeLogarithmicMultiplier()

		def mod(self, num) : 
			if num < 0 : 
				return -num
			return num

		def checkIfLessThanOrEqual(self, n1, n2) : 
			if n2 <= n1 : 
				return True
			return False

		def testOperation(self) : 
			# for i in range(100000) : 
			# 	n1 = random.randint(1, 100000000)
			# 	n2 = random.randint(1, 100000000)
			# 	k1 = int(self.multiplier.priorityEncoder(bin(n1)[2:]), base=2)
			# 	k2 = int(self.multiplier.priorityEncoder(bin(n2)[2:]), base=2)
			# 	p0_1 = self.multiplier.p0_1(bin(n1)[2:], bin(n2)[2:])
			# 	p0_2 = self.multiplier.p0_2(bin(n1)[2:], bin(n2)[2:])
			# 	p0_3 = self.multiplier.p0_3(bin(n1)[2:], bin(n2)[2:])
			# 	# p0_1 = 2**(k1+k2)
			# 	# p0_2 = (2**k2)*(n1 - (2**k1))
			# 	# p0_3 = (2**k1)*(n2 - (2**k2))
			# 	t1 = self.multiplier.add(self.multiplier.p0_1(bin(n1)[2:], bin(n2)[2:]), self.multiplier.p0_2(bin(n1)[2:], bin(n2)[2:]))
			# 	t1 = t1[1] + t1[0]
			# 	t2 = self.multiplier.add(self.multiplier.p0_3(bin(n1)[2:], bin(n2)[2:]), t1)
			# 	t2 = t2[1] + t2[0]
			# 	p0_approx = int(t2, base=2)

			# 	# p0_approx = int(p0_1, base=2) + int(p0_2, base=2) + int(p0_3, base=2)
			# 	p0_exact = n1*n2
				
			# 	print(str(n1) + ' * ' + str(n2) + ' -- ' + str(p0_exact) + ' / ' + str(p0_approx))
			# 	self.assertEqual(self.checkIfLessThanOrEqual(p0_exact, p0_approx), True)

			for i in range(10000) : 
				n1 = random.randint(1, 10000)
				n2 = random.randint(1, 10000)
				result_reqd = n1*n2
				result_getd = self.multiplier.p0_approx(bin(n1)[2:], bin(n2)[2:])
				self.assertEqual(self.multiplier.validateBinary(result_getd), True)

				def checkIfLessThan(n1, n2) : 
					if n2 < n1 :
						return True
					return False

				relativeError = self.mod(result_reqd - int(result_getd, base=2))*1.0 / result_reqd
				print(str(n1) + ' * ' + str(n2) + ' -- ' + str(result_reqd) + ' / ' + str(int(result_getd, base=2)) + ' -- ' + str(relativeError))

				self.assertEqual(self.checkIfLessThanOrEqual(result_reqd, int(result_getd, base=2)), True)

	class ValidateBinary(unittest.TestCase) : 

		def setUp(self) : 
			self.multiplier = IntegerIterativeLogarithmicMultiplier()

		def testOperation(self) : 
			self.assertEqual(self.multiplier.validateBinary('1000010101010'), True)
			self.assertEqual(self.multiplier.validateBinary(''), False)
			self.assertEqual(self.multiplier.validateBinary('4'), False)
			self.assertEqual(self.multiplier.validateBinary('100101010002'), False)
			self.assertEqual(self.multiplier.validateBinary('1000s'), False)

		def testErrors(self) : 
			self.assertRaises(AssertionError, self.multiplier.validateBinary, 10)

	class PriorityEncoder(unittest.TestCase) :

		def setUp(self) : 
			self.multiplier = IntegerIterativeLogarithmicMultiplier()

		def testOperation(self) : 

			self.assertEqual(self.multiplier.priorityEncoder('00000001'), '000')

			self.assertEqual(self.multiplier.priorityEncoder('00000010'), '001')
			self.assertEqual(self.multiplier.priorityEncoder('00000011'), '001')

			self.assertEqual(self.multiplier.priorityEncoder('00000100'), '010')
			self.assertEqual(self.multiplier.priorityEncoder('00000110'), '010')
			self.assertEqual(self.multiplier.priorityEncoder('00000101'), '010')
			self.assertEqual(self.multiplier.priorityEncoder('00000111'), '010')

			self.assertEqual(self.multiplier.priorityEncoder('10000000'), '111')
			self.assertEqual(self.multiplier.priorityEncoder('10100000'), '111')
			self.assertEqual(self.multiplier.priorityEncoder('11001000'), '111')
			self.assertEqual(self.multiplier.priorityEncoder('11000001'), '111')

			self.assertEqual(self.multiplier.priorityEncoder('01000000'), '110')
			self.assertEqual(self.multiplier.priorityEncoder('01001000'), '110')
			self.assertEqual(self.multiplier.priorityEncoder('01100000'), '110')
			self.assertEqual(self.multiplier.priorityEncoder('01001001'), '110')

			self.assertEqual(self.multiplier.priorityEncoder('00100000'), '101')
			self.assertEqual(self.multiplier.priorityEncoder('00110000'), '101')
			self.assertEqual(self.multiplier.priorityEncoder('00111000'), '101')
			self.assertEqual(self.multiplier.priorityEncoder('00100001'), '101')

			self.assertEqual(self.multiplier.priorityEncoder('00010000'), '100')
			self.assertEqual(self.multiplier.priorityEncoder('00010100'), '100')
			self.assertEqual(self.multiplier.priorityEncoder('00011001'), '100')
			self.assertEqual(self.multiplier.priorityEncoder('00010001'), '100')

			self.assertEqual(self.multiplier.priorityEncoder('00001000'), '011')
			self.assertEqual(self.multiplier.priorityEncoder('00001100'), '011')
			self.assertEqual(self.multiplier.priorityEncoder('00001010'), '011')
			self.assertEqual(self.multiplier.priorityEncoder('00001011'), '011')

	class Decoder(unittest.TestCase) : 

		def setUp(self) : 
			self.multiplier = IntegerIterativeLogarithmicMultiplier()

		def testOperation(self) : 
			self.assertEqual(self.multiplier.decoder('000'), '00000001')
			self.assertEqual(self.multiplier.decoder('001'), '00000010')
			self.assertEqual(self.multiplier.decoder('010'), '00000100')
			self.assertEqual(self.multiplier.decoder('011'), '00001000')
			self.assertEqual(self.multiplier.decoder('100'), '00010000')
			self.assertEqual(self.multiplier.decoder('101'), '00100000')
			self.assertEqual(self.multiplier.decoder('110'), '01000000')
			self.assertEqual(self.multiplier.decoder('111'), '10000000')

			randomNumbers = ['10000', '1', '00000010000', '001', '00000100000', '010']
			for number in randomNumbers : 
				self.assertEqual(int(self.multiplier.decoder(self.multiplier.priorityEncoder(number)), base=2), int(number, base=2))

	class ClearBit(unittest.TestCase) : 

		def setUp(self) : 
			self.multiplier = IntegerIterativeLogarithmicMultiplier()

		def testOperation(self) : 
			self.assertEqual(self.multiplier.validateBinary(self.multiplier.clearBit('10001010', 1)), True)
			self.assertEqual(self.multiplier.validateBinary(self.multiplier.clearBit('1000000000000001', 15)), True)
			self.assertEqual(self.multiplier.clearBit('10001010', 1), '10001000')
			self.assertEqual(self.multiplier.clearBit('1000000000000001', 15), '0000000000000001')

		def testErrors(self) : 
			self.assertRaises(AssertionError, self.multiplier.clearBit, '10010', 's')
			self.assertRaises(AssertionError, self.multiplier.clearBit, '10000', -10)
			self.assertRaises(AssertionError, self.multiplier.clearBit, '100', 3)

	class ShiftLeft(unittest.TestCase) : 

		def setUp(self) : 
			self.multiplier = IntegerIterativeLogarithmicMultiplier()

		def testOperation(self) : 
			testPairs = [
				['10010100', 3], 
				['1001010010101010100', 0],
				['10', 64]
			]
			for testPair in testPairs : 
				self.assertEqual(self.multiplier.validateBinary(self.multiplier.shiftLeft(testPair[0], testPair[1])), True)
			self.assertEqual(self.multiplier.shiftLeft('10010100', 3), '10100000')
			self.assertEqual(self.multiplier.shiftLeft('1001010010101010100', 0), '1001010010101010100')
			self.assertEqual(self.multiplier.shiftLeft('10', 64), '00')
			self.assertEqual(self.multiplier.shiftLeft('100100100101000101010010010100101001010001011', 44), '100000000000000000000000000000000000000000000')

		def testErrors(self) : 
			self.assertRaises(AssertionError, self.multiplier.shiftLeft, '10001010', -2)

	class Add(unittest.TestCase) : 

		def setUp(self) : 
			self.multiplier = IntegerIterativeLogarithmicMultiplier()

		def testOperation(self) : 
			for i in range(10000) : 	
				n1 = random.randint(0, 1000000000000000000)
				n2 = random.randint(0, 1000000000000000000)
				sum_, carry = self.multiplier.add(bin(n1)[2:], bin(n2)[2:])
				self.assertEqual(self.multiplier.validateBinary(carry), True)
				self.assertEqual(self.multiplier.validateBinary(sum_), True)
				self.assertEqual(int(carry + sum_, base=2), n1+n2)

	class P0_1(unittest.TestCase) : 

		def setUp(self) : 
			self.multiplier = IntegerIterativeLogarithmicMultiplier()

		def testOperation(self) : 
			for i in range(1000) : 
				n1 = random.randint(1, 100)
				n2 = random.randint(1, 100)
				k1 = int(self.multiplier.priorityEncoder(bin(n1)[2:]), base=2)
				k2 = int(self.multiplier.priorityEncoder(bin(n2)[2:]), base=2)
				p0_1_reqd = 2**(k1+k2)
				p0_1_getd = self.multiplier.p0_1(bin(n1)[2:], bin(n2)[2:])
				self.assertEqual(self.multiplier.validateBinary(p0_1_getd), True)
				self.assertEqual(p0_1_reqd, int(p0_1_getd, base=2))

	class P0_2(unittest.TestCase) : 

		def setUp(self) : 
			self.multiplier = IntegerIterativeLogarithmicMultiplier()

		def testOperation(self) : 
			for i in range(1000) : 
				n1 = random.randint(1, 100)
				n2 = random.randint(1, 100)
				k1 = int(self.multiplier.priorityEncoder(bin(n1)[2:]), base=2)
				k2 = int(self.multiplier.priorityEncoder(bin(n2)[2:]), base=2)
				p0_2_reqd = (n1-(2**k1))*(2**k2)
				p0_2_getd = self.multiplier.p0_2(bin(n1)[2:], bin(n2)[2:])
				self.assertEqual(self.multiplier.validateBinary(p0_2_getd), True)
				self.assertEqual(p0_2_reqd, int(p0_2_getd, base=2))

	class P0_3(unittest.TestCase) : 

		def setUp(self) : 
			self.multiplier = IntegerIterativeLogarithmicMultiplier()

		def testOperation(self) : 
			for i in range(1000) : 
				n1 = random.randint(1, 100)
				n2 = random.randint(1, 100)
				k1 = int(self.multiplier.priorityEncoder(bin(n1)[2:]), base=2)
				k2 = int(self.multiplier.priorityEncoder(bin(n2)[2:]), base=2)
				p0_3_reqd = (n2-(2**k2))*(2**k1)
				p0_3_getd = self.multiplier.p0_3(bin(n1)[2:], bin(n2)[2:])
				self.assertEqual(self.multiplier.validateBinary(p0_3_getd), True)
				self.assertEqual(p0_3_reqd, int(p0_3_getd, base=2))

class TestFloatingPointIterativeLogarithmicMultiplier() :
	
	class getBinarySignificand(unittest.TestCase) : 

		def testErrors(self) : 
			multiplier = FloatingPointIterativeLogarithmicMultiplier()
			multiplier.getBinarySignificand(Float())
			self.assertRaises(AssertionError, multiplier.getBinarySignificand, 10)

if __name__ == '__main__' : 

	def runSuite(suite) : 
		suite = unittest.TestLoader().loadTestsFromTestCase(suite)
		ColourTextTestRunner(verbosity=2).run(suite)

	suiteList = [
		# TestIntegerIterativeLogarithmicMultiplier.Constructor,
		# TestIntegerIterativeLogarithmicMultiplier.Multiply, 
		TestIntegerIterativeLogarithmicMultiplier.P0_approx,
		# TestIntegerIterativeLogarithmicMultiplier.ValidateBinary,
		# TestIntegerIterativeLogarithmicMultiplier.PriorityEncoder,
		# TestIntegerIterativeLogarithmicMultiplier.Decoder,
		# TestIntegerIterativeLogarithmicMultiplier.ClearBit,
		# TestIntegerIterativeLogarithmicMultiplier.ShiftLeft, 
		# TestIntegerIterativeLogarithmicMultiplier.Add, 
		# TestIntegerIterativeLogarithmicMultiplier.P0_1,
		# TestIntegerIterativeLogarithmicMultiplier.P0_2,
		# TestIntegerIterativeLogarithmicMultiplier.P0_3,
		# TestFloatingPointIterativeLogarithmicMultiplier.getBinarySignificand
	]

	for suite in suiteList : 
		runSuite(suite)