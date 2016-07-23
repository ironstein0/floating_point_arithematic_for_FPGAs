#!/usr/bin/Python
from bitstring import bitstring as bs

class Float(bs.BitArray) :
	'''
	Extends the bitstring.BitArray class by implementing 
	floating point number specific methods 
	
	:methods: 

	:attributes:
		float
		bin
		raw_mantissa
		raw_exponent
		exponent_field
		exponent_value
		raw_sign
	'''

	def __init__(self, num=0, length=32) :
		self._float = self._getfloat()
		self._bin = self._convert_bin_to_readable(self._getbin())

	def __new__(cls, num=0, length=32) :
		if length != 32 and length != 64 : 
			raise bs.CreationError('invalid length "{0}"; only lengths "32" and "64" allowed.'.format(str(length)))
		f = super(Float, cls).__new__(cls, float=num, length=length)
		return f

	""" float """
	@property
	def float(self):
		return self._getfloat()

	@float.setter
	def float(self, num) : 
		x = super(bs.BitArray, self).__new__(self.__class__, float=num, length=self.len)
		self._datastore = x._datastore

	""" bin """
	@property
	def bin(self):
		return self._convert_bin_to_readable(self._getbin())
	
	@bin.setter
	def bin(self, string) : 
		if len(string) != 32 and len(string) != 64 : 
			raise bs.CreationError('invalid length "{0}"; only lengths "32" and "64" allowed.'.format(str(len(string))))
		x = super(bs.BitArray, self).__new__(self.__class__, bin=string)
		self._datastore = x._datastore

	def _convert_bin_to_readable(self, string) :
		sep = '_'
		return_string =  string[0] + sep + self.raw_exponent + sep
		mantissa = self.raw_mantissa
		for i in range(len(mantissa)) : 
			if not(i%8) : 
				return_string += '.'
			return_string += mantissa[i]
		return return_string

	""" MANTISSA """
	# raw_mantissa
	@property
	def raw_mantissa(self):
		if self.len == 32 : 
			return self._getbin()[9:]
		return self._getbin()[11:]

	""" EXPONENT """
	# raw_exponent
	@property
	def raw_exponent(self):
		if self.len == 32 : 
			return self._getbin()[1:9]
		return self._getbin()[1:12]

	# exponent_field
	@property
	def exponent_field(self):
		return int(self.raw_exponent, 2)

	# exponent_value
	@property
	def exponent_value(self):
		return 127 - self.exponent_field

	""" SIGN """
	# raw_sign
	@property 
	def raw_sign(self) : 
		return self._getbin()[0]
