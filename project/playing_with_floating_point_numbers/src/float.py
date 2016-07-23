#!/usr/bin/Python
from bitstring import bitstring as bs

class Float(bs.BitArray) :
	'''
	Extends the bitstring.BitArray class by implementing 
	floating point number specific methods 
	'''

	def __init__(self, num=0, length=32) :
		pass

	def __new__(cls, num=0, length=32) :
		if length != 32 and length != 64 : 
			raise bs.CreationError('invalid length "{0}"; only lengths "32" and "64" allowed.'.format(str(length)))
		f = super(Float, cls).__new__(cls, float=num, length=length)
		return f

	# value
	@property
	def value(self):
		return self.float

	@value.setter
	def value(self, num) : 
		x = super(bs.BitArray, self).__new__(self.__class__, float=num, length=self.len)
		self._datastore = x._datastore

	# raw_mantissa
	@property
	def raw_mantissa(self):
		if self.len == 32 : 
			return self.bin[9:]
		return self.bin[11:]

	# raw_exponent
	@property
	def raw_exponent(self):
		if self.len == 32 : 
			return self.bin[1:9]
		return self.bin[1:12]

	# raw_sign
	@property 
	def raw_sign(self) : 
		return self.bin[0]
	