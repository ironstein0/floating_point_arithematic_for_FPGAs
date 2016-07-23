#!/usr/bin/Python
from bitstring import bitstring as bs

class Float(bs.BitArray) :

	def __init__(self, num=0, length=32) :
		pass

	def __new__(cls, num=0, length=32) :
		if length != 32 and length != 64 : 
			raise bs.CreationError('invalid length "{0}"; only lengths "32" and "64" allowed.'.format(str(length)))
		f = super(Float, cls).__new__(cls, float=num, length=length)
		return f

	@property
	def value(self):
		return self.float