#!/usr/bin/Python
from Float import Float
import utils

class IntegerIterativeLogarithmicMultiplier() : 
	"""Python implementation of the Iterative Logarithmic Multipler

	Based on work by Zdenka Babic, Aleksej Avramovic and Patricio Bulic	
	.. _An Iterative Logarithmic Multiplier
	   http://ev.fe.uni-lj.si/1-2010/Babic.pdf
	
	Methods: 

	Attributes:

	"""

	''' 
	TODO : 
		wherever int(blah, base=2) is used, replace it with logic
	'''

	def __init__(self) : 
		pass

	def multiply(self, n1, n2, correctionIterations) : 
		"""Multiply two floating point numbers

		Args: 
			n1 (str) 
			n2 (str)

		Returns: 
			str -- A binary string representing the multiplicaiton of n1 and n2

		Raises:
			ValueError -- if n1, n2 are not strings
			ValueError -- if n1, n2 are not valid binary strings

		"""

		if not isinstance(n1, str) or not isinstance(n2, str) : 
			raise ValueError('n1 and n2 should be an instances of Float')

		if not self.validateBinary(n1) or not self.validateBinary(n2) : 
			raise ValueError('n1 and n2 should be valid binary strings')

		product = '0'
		for iterationNumber in range(correctionIterations) : 
			k1 = int(self.priorityEncoder(n1), base=2)
			k2 = int(self.priorityEncoder(n2), base=2)
			p0_approx = self.add(product, self.p0_approx(n1, n2))
			product = self.add(product, p0_approx[1] + p0_approx[0])
			product = product[1] + product[0]
			n1 = self.clearBit(n1, k1)
			n2 = self.clearBit(n2, k2)

			if int(n1, base=2) == 0 or int(n2, base=2) == 0 : 
				break
		return product

	def p0_approx(self, n1, n2) : 
		assert self.validateBinary(n1)
		assert self.validateBinary(n2)

		p0_1 = self.p0_1(n1, n2)
		p0_2 = self.p0_2(n1, n2)
		p0_3 = self.p0_3(n1, n2)
		t1 = self.add(self.p0_1(n1, n2), self.p0_2(n1, n2))
		t1 = t1[1] + t1[0]
		t2 = self.add(self.p0_3(n1, n2), t1)
		t2 = t2[1] + t2[0]
		return t2

	def p0_1(self, n1, n2) : 
		# find 2**(k1+k2)
		k1 = self.priorityEncoder(n1)
		k2 = self.priorityEncoder(n2)
		k12 = self.add(k1, k2)
		k12 = k12[1] + k12[0] 	# carry + sum
		p0_1 = self.decoder(k12)
		return p0_1

	def p0_2(self, n1, n2) :
		# find (2**k2)*(n1 - 2**k1)

		# k2
		t1 = self.priorityEncoder(n2)
		# n1 - 2**k1
		t2 = self.clearBit(n1, int(self.priorityEncoder(n1), base=2))
		p0_2 = self.shiftLeft(t2, int(t1, base=2), len(n1) + len(n2))
		return p0_2

	def p0_3(self, n1, n2) : 
		# find (2**p1)*(n2 - 2**p2)

		# k2
		t1 = self.priorityEncoder(n1)
		# n2 - 2**k2
		t2 = self.clearBit(n2, int(self.priorityEncoder(n2), base=2))
		p0_3 = self.shiftLeft(t2, int(t1, base=2), len(n1) + len(n2))
		return p0_3

	def validateBinary(self, n) : 
		assert isinstance(n, str)
		if len(n) == 0 : 
			return False

		for element in n : 
			if element != '0' and element != '1' : 
				return False
		return True

	def priorityEncoder(self, n) : 
		assert self.validateBinary(n) == True
		minNumberOfEncodedBits = 1
		while 2**minNumberOfEncodedBits < len(n) : 
			minNumberOfEncodedBits += 1

		for i in range(len(n)) : 
			j = i
			if n[i] == '1' :
				break

		encodedValue = bin(len(n) - j - 1)[2:]

		encodedValue = (minNumberOfEncodedBits - len(encodedValue))*'0' + encodedValue
		return encodedValue

	def decoder(self, n) : 
		assert self.validateBinary(n) == True
		numberOfDecodedBits = 2**(len(n))
		encodedValue = bin(2**(int(n, base=2)))[2:]
		encodedValue = (numberOfDecodedBits - len(encodedValue))*'0' + encodedValue
		return encodedValue

	def clearBit(self, n, bitNumber) : 
		assert self.validateBinary(n)
		assert type(bitNumber) == int
		assert bitNumber >= 0
		assert bitNumber < len(n)
		bitToClear = len(n) - bitNumber - 1
		return n[:bitToClear] + '0' + n[bitToClear+1:]

	def shiftLeft(self, n, bitsToShift, numberOfBitsInResult=None) : 
		assert self.validateBinary(n)
		assert bitsToShift >= 0
		shiftedValue = bin(int(n, base=2)*(2**bitsToShift))[2:]
		if numberOfBitsInResult == None : 
			numberOfBitsInResult = len(n)
		if len(shiftedValue) <= numberOfBitsInResult : 
			shiftedValue = (numberOfBitsInResult - len(shiftedValue))*'0' + shiftedValue
		else : 
			shiftedValue = shiftedValue[len(shiftedValue) - numberOfBitsInResult:]
		return shiftedValue

	def add(self, n1, n2) : 
		assert self.validateBinary(n1)
		assert self.validateBinary(n2)

		sum_ = bin(int(n1, base=2) + int(n2, base=2))[2:]
		carry = '0'
		sumLength = max(len(n1), len(n2))
		if len(sum_) <= sumLength : 
			sum_ = (sumLength -len(sum_))*'0' + sum_
		else : 
			carry = sum_[0]
			sum_ = sum_[1:]
		return [sum_, carry]

class FloatingPointIterativeLogarithmicMultiplier() : 

	def __init__(self) : 
		pass

	def getBinarySignificand(self, f) : 
		assert isinstance(f, Float)
		return '1' + f.raw_mantissa