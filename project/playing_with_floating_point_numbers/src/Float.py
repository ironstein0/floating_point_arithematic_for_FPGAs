#!/usr/bin/Python
from bitstring import bitstring as bs

class Float(bs.BitArray) :
	"""Extends the bitstring.BitArray class by implementing floating point number specific methods 

	Inherits most of the methods from bitstring.BitArray class
	Provides additional floating point arithematic specific attributes and methods
	
	Methods: 

	Attributes:
		float (float) -- `float` value corresponding to the Float instance
		bin (str) -- binary `str` representing the float attribute
		raw_mantissa (str) -- `str` representation of binary mantissa of bin
		raw_exponent (str) -- `str` representation of binary exponent of bin
		exponent_field (int) -- exponent field of float
		exponent_value (int) -- exponent value (biased) of float
		raw_sign (str) -- string representation of binary sign of bin

	"""

	def __init__(self, num=0, length=32) :
		"""
		Args: 
			num (float|int|str) -- number that the Float instance shall represent
			length (int) -- length of the binary value representing the Float instace (32 or 64)

		Raises: 
			bitstring.CreationError -- if num is not a `float`, `int` or `str`
			bitstring.CreationError -- if num is `str` and its length is neither 32 nor 64
			bitstring.CreationError -- if num is `str` but does not represent a valid binary number
			bitstring.CreationError -- if length is neither 32 nor 64

		"""

		pass

	def __new__(cls, num=0, length=32) :
		"""
		Overrides __new__ method of bitstring.BitArray to implement stricter type checking

		"""
		
		# invalid length
		if length != 32 and length != 64 : 
			raise bs.CreationError('invalid length "{0}"; only lengths "32" and "64" allowed.'.format(str(length)))

		if type(num) == int or type(num) == float : 
			f = super(Float, cls).__new__(cls, float=num, length=length)
			return f
		elif type(num) == str : 
			f = super(Float, cls).__new__(cls, float=0, length=length)
			f.bin = num
			return f

		# invalid type
		raise bs.CreationError('invalid type "{0}" of num'.format(type(num)))

	@property
	def float(self):
		""" float -- `float` representation of the Float instance
		
		Raises:
			bitstring.CreationError -- when assigning value that is neither `float` nor `int`

		"""

		return self._getfloat()

	@float.setter
	def float(self, num) : 
		if type(num) != float and type(num) != int: 
			raise bs.CreationError('invalid type "{0}" of num'.format(type(num)))
		x = super(bs.BitArray, self).__new__(self.__class__, float=num, length=self.len)
		self._datastore = x._datastore

	@property
	def bin(self):
		""" str -- binary representation of the float attribute

		Raises:
			bitstring.CreationError -- when assigning value that is not a `str`
			bitstring.CreationError -- when assigning value that does not 
				represent a valid binary value
			bitstring.CreationError -- when assigning value whose length is neither 32 nor 64

		"""

		return self._getbin()
	
	@bin.setter
	def bin(self, binString) : 
		if type(binString) != str : 
			raise bs.CreationError('invalid type "{0} of binString'.format(type(binString)))
		if len(binString) != self.len : 
			error_string = 'invalid length "{0}";'.format(str(len(binString)))
			raise bs.CreationError(error_string + ' only lengths "32" and "64" allowed.')
		x = super(bs.BitArray, self).__new__(self.__class__, bin=binString)
		self._datastore = x._datastore

	@property
	def bin_readable(self):
		""" str -- readable binary string representing the Float instance 

		sign_exponent_mantiss (mantissa seprarted by '.' at intervals of 8 bits)
		for example '1_10010110_10101010.10101010.10101010'
					<S><- EXP-> <------- MANTISSA ------->

		"""

		sep = '_'
		return_string = self.raw_sign + sep + self.raw_exponent + sep
		mantissa = self.raw_mantissa
		for i in range(len(mantissa)) : 
			if not(i%8) : 
				return_string += '.'
			return_string += mantissa[i]
		return_string_list = return_string.split(sep + '.')
		return_string = return_string_list[0] + sep + return_string_list[1]
		return return_string

	# TODO : 
	'''	setters for 
			raw_mantissa
			raw_exponent
			raw_sign
	'''

	@property
	def raw_mantissa(self):
		""" str -- binary string representation of the mantissa of the Float instance
		
		Raises: 
			bitstring.CreationError -- when assigning a value that is not `str`
			bitstring.CreationError -- when assigning a string with length neither 23 nor 52

		"""
		if self.len == 32 : 
			return self._getbin()[9:]
		return self._getbin()[12:]

	@raw_mantissa.setter
	def raw_mantissa(self, raw_mantissa) : 
		if type(raw_mantissa) != str : 
			raise bs.CreationError('invalid type "{0}" for mantissa'.format(type(raw_mantissa)))
		if self.len == 32 : 
			if len(raw_mantissa) != 23 : 
				raise bs.CreationError('expected mantissa to be 23 bits long')
		else : 
			if len(raw_mantissa) != 52 : 
				raise bs.CreationError('expected mantissa to be 52 bits long')
		self.bin = self.raw_sign + self.raw_exponent + raw_mantissa

	@property
	def raw_exponent(self):
		""" str -- binary string representation of the exponent of the Float instance
		
		Raises: 
			bitstring.CreationError -- when assigning value that is not `str`
			bitstring.CreaionError -- when assigning a string with length neither 8 nor 11

		"""
		if self.len == 32 : 
			return self._getbin()[1:9]
		return self._getbin()[1:12]

	@raw_exponent.setter
	def raw_exponent(self, raw_exponent) :
		if type(raw_exponent) != str : 
			raise bs.CreationError('invalid type "{0}" for mantissa'.format(type(raw_exponent)))
		if self.len == 32 : 
			if len(raw_exponent) != 8 : 
				raise bs.CreationError('expected exponent to be 8 bits long')
		else : 
			if len(raw_exponent) != 11 : 
				raise bs.CreationError('expected exponent to be 11 bits long')
		self.bin = self.raw_sign + raw_exponent + self.raw_mantissa

	@property
	def exponent_field(self):
		""" int -- raw exponent field value"""
		return int(self.raw_exponent, 2)

	@property
	def exponent_value(self):
		""" int -- biased exponent value"""
		if self.len == 32 : 
			return self.exponent_field - 127
		else : 
			return self.exponent_field - 1023

	@property 
	def raw_sign(self) : 
		""" str -- string representation of raw sign bit of the Float instance"""
		return self._getbin()[0]

	@raw_sign.setter
	def raw_sign(self, raw_sign) : 
		if type(raw_sign) != str : 
			raise bs.CreationError('invalid type "{0}" for sign')
		if len(raw_sign) != 1 : 
			raise bs.CreationError('expected sign to be 1 bits long')
		self.bin = raw_sign + self.raw_exponent + self.raw_mantissa
