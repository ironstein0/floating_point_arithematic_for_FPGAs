#!/usr/bin/Python
from bitstring import bitstring as bs

class Float(bs.BitArray) :
	"""Extends the bitstring.BitArray class by implementing 
	floating point number specific methods 
	
	Methods: 

	Attributes:
		float
		bin
		raw_mantissa
		raw_exponent
		exponent_field
		exponent_value
		raw_sign
	"""

	def __init__(self, num=0, length=32) :
		self._float = self._getfloat()
		self._bin = self._convert_bin_to_readable(self._getbin())

	def __new__(cls, num=0, length=32) :
		if type(num) != int and type(num) != float : 
			raise bs.CreationError('invalid type "{0}" of num'.format(type(num)))
		if length != 32 and length != 64 : 
			raise bs.CreationError('invalid length "{0}"; only lengths "32" and "64" allowed.'.format(str(length)))
		f = super(Float, cls).__new__(cls, float=num, length=length)
		return f

	@property
	def float(self):
		""" float: float representation of the Float instance"""
		return self._getfloat()

	@float.setter
	def float(self, num) : 
		""" change the value of the Float instance, by passing in a float value

		Args:
			num (float|int): a float value

		Returns: 
			None

		Raises:
			bitstring.bitstring.CreationError: If num is not a `float`

		"""
		if type(num) != float and type(num) != int: 
			raise bs.CreationError('invalid type "{0}" of num'.format(type(num)))
		x = super(bs.BitArray, self).__new__(self.__class__, float=num, length=self.len)
		self._datastore = x._datastore

	@property
	def bin(self):
		""" str: binary representation of the Float instance"""
		return self._convert_bin_to_readable(self._getbin())
	
	@bin.setter
	def bin(self, binString) : 
		""" change the value of the Float by passing in a binary value

		Args: 
			binString (str): a string of length 32 or 64 representing a binary number

		Returns: 
			None

		Raises:
			bitstring.bitstring.CreationError: If binString is not a `str`
			bitstring.bitstring.CreationError: If binString does not represent a valid binary value

		"""
		if type(binString) != str : 
			raise bs.CreationError('invalid type "{0} of binString'.format(type(binString)))
		if len(binString) != 32 and len(binString) != 64 : 
			raise bs.CreationError('invalid length "{0}"; only lengths "32" and "64" allowed.'.format(str(len(binString))))
		x = super(bs.BitArray, self).__new__(self.__class__, bin=binString)
		self._datastore = x._datastore

	def _convert_bin_to_readable(self, string) :
		""" converts a binary string to human readable format
	
		Args: 
			binString (str): string representation of a binary number

		Returns: 
			str: formatted readable binary string

		"""
		sep = '_'
		return_string =  string[0] + sep + self.raw_exponent + sep
		mantissa = self.raw_mantissa
		for i in range(len(mantissa)) : 
			if not(i%8) : 
				return_string += '.'
			return_string += mantissa[i]
		return return_string

	@property
	def raw_mantissa(self):
		""" str: string representation of the mantissa of the Float instance"""
		if self.len == 32 : 
			return self._getbin()[9:]
		return self._getbin()[11:]

	@property
	def raw_exponent(self):
		""" str: string representation of the exponent of the Float instance"""
		if self.len == 32 : 
			return self._getbin()[1:9]
		return self._getbin()[1:12]

	@property
	def exponent_field(self):
		""" int: raw exponent field value"""
		return int(self.raw_exponent, 2)

	@property
	def exponent_value(self):
		""" int: biased exponent value"""
		return 127 - self.exponent_field

	@property 
	def raw_sign(self) : 
		""" str: string representation of raw sign bit of the Float instance"""
		return self._getbin()[0]
