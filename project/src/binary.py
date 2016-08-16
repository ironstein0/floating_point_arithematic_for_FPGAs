class Binary : 

	def __init__(
		self, 
		num, 
		truncate=False, 
		raise_error_on_truncate=True,
		number_of_bits=32, 
		number_of_bits_before_decimal=32, 
		number_of_bits_after_decimal=64) : 
		'''
		:expects:
			num : 				integer or float variable, or a string 
								representation of a float
			truncate : 			if set True, the binary intgral value (
								only the integer part in case of fraction)
								will be truncated to fit the number of bits
								specified ('number_of_bits' in case of integer, 
								and 'number_of_bits_before_decimal' in case of
								float). In case of floats, number of bits
								after decimal will always be truncated.
			number_of_bits : 	number of bits in the binary representation 
		'''

		# check the type of "num" and convert to binary string accordingly
		self.__num = num
		self.__truncate = truncate
		self.__raise_error_on_truncate = raise_error_on_truncate
		if type(num) == int : 
			self.__number_of_bits = number_of_bits
			self.__string_representation = str(num)
			self.__binary_string = ('{0:0' + str(number_of_bits) + 'b}').format(num)
			self.__type__ = int
		elif type(num) == float : 
			self.__number_of_bits_before_decimal = number_of_bits_before_decimal
			self.__number_of_bits_after_decimal = number_of_bits_after_decimal
			self.__string_representation = self.get_string_representation_for_float(num)
			self.__binary_string = self.get_binary_from_float(num)
			self.__type__ = float
		elif type(num) == str :
			self.check_if_properly_formatted_float_string(num)
			self.__number_of_bits_before_decimal = number_of_bits_before_decimal
			self.__number_of_bits_after_decimal = number_of_bits_after_decimal
			self.__string_representation = num
			self.__binary_string = self.get_binary_from_float(float(num))
			self.__type__ = float
		else : 
			raise ValueError('invalid type : ' + type(num))

	def check_if_properly_formatted_float_string(self, string) : 
		'''
		:raises:
			ValueError if the format of the string passed does not 
			confirm to that of a float
		'''
		dot_count = 0
		error_string = 'improperly formatted float string : ' + string
		for character in string : 
			if not((ord(character) >= 48) and (ord(character) <= 57)) : 
				# 48 => 0 and 57 => 9
				if character == '.' : 
					dot_count += 1
					if dot_count > 1 : 
						raise ValueError(error_string)
				else : 
					raise ValueError(error_string)
		if dot_count == 0 : 
			raise ValueError(error_string)


	def get_string_representation_for_float(num) :
		'''
		:returns:
			string decimal representation for the floating point number 'num'

		##############################
		# test cases
		##############################
		1.23654233 				=> 	'1.23654233'
		10000000000000.23654233 => 	'10000000000000.0'
		1e-29					=> 	'0.00000000000000000000000000001'
		1e29 					=> 	'100000000000000000000000000000.0'
		'''

		print(num)
		if 'e' in str(num) : 
			# scientific notation
			significand, exponent = str(num).split('e')
			if '.' not in significand : 
				significand += '.0'
			exponent = int(exponent) 
			length = 0
			if exponent < 0 : 
				length = len(significand.split('.')[-1]) + abs(exponent)
				return format(num, '.' + str(length - 1) + 'f')
			else : 
				integer = ''
				for element in significand : 
					if element != '.' : 
						integer += element
				print('integer - ' + integer)
				if exponent >= len(significand.split('.')[-1]) : 					
					return integer + '0'*(exponent - len(significand.split('.')[-1])) + '.0'
				else : 
					decimal_position = len(significand.split('.')[0]) + exponent
					integer = integer[:decimal_position] + '.' + integer[decimal_position:]

		else : 
			# decimal notation
			return str(num)

	def get_binary_from_float(self, num) :
		'''
		:expects:
			num : a float
		:returns: 
			a string representing the float value in base 2 binary form
			for example : decimal"0.125" is represented as binary"0.001"
		''' 
		if type(num) != float : 
			raise ValueError('expected float, but received : ' + type(num))

		def get_fraction_string(num) : 
			'''
			:raises:
				RuntimeError if : 
					- truncate = self.__truncate == True
					- self.__raise_error_on_truncate == True
					- length binary value of the integral part of 'num' is greater
					  than self.__number_of_bits_before_decimal
			:returns:
				string representing only the fraction part of the float
				for example : for num = 10.455, returns '0.455'
			
			tested for values of num from -1000000000 to 1000000000
			'''
			if type(num) == int : 
				return float(0)
			fraction_num_str = '0.' + str(num).split('.')[-1]
			if num < 0 : 
				fraction_num_str = '-' + fraction_num_str
			print('fraction_num_str = ' + fraction_num_str)
			return fraction_num_str
			# if(float_) : 
			# 	pass
			# number_of_fraction_digits = len(str(num).split('.')[-1])
			# if float_num > 0 : 
			# 	return float(str(float_num)[:number_of_fraction_digits+2])
			# else : 
			# 	return float(str(float_num)[1:number_of_fraction_digits+3])

		integer = int(num)
		fraction_string = get_fraction_string(num)

		integer_bin = bin(integer)[2:]
		if (self.__truncate == True) and (len(integer_bin) > self.__number_of_bits_before_decimal) : 
			if self.__raise_error_on_truncate : 
				raise RuntimeError('Overflow when converting float : ' + str(num) + ' to binary')
			print('Warning : Overflow when converting float : ' + str(num) + ' to binary')
			integer_bin = integer_bin[len(integer_bin)-number_of_bits_before_decimal-1:]

		if num < 0 : 
			integer_bin = '-' + integer_bin[1:]

		print(integer_bin)

		fraction_bin = ''
		fraction_temp = 0
		for i in range(1, self.__number_of_bits_after_decimal+1) : 
			if str(fraction_temp + (2**(-i))) < fraction_string : 
				fraction_bin += '1'
				fraction_temp += 2**(-i)
			else : 
				fraction_bin += '0'
		print(fraction_bin)

	def convert_float_to_interchange_format(self, interchange_format='bin32') :

		'''
		:expects:
			interchange format : could be 'bin32', 'bin64'
		:returns:
			None
		converts the __binary_string to IEEE 754 - 2008 interchange
		format representation
		'''
		if type(self.__num) != float : 
			error_string = 'Binary object does not represent a float, can not'
			error_string += 'call method "convert_float_to_interchange_format" '
			error_string += 'on this object'
			raise ValueError(error_string)

		if intechange_format != 'bin32' and interchange_format != 'bin64' : 
			raise ValueError('invalid format : ' + intechange_format)



	def get_binary_string(self) : 
		return self.__binary_string

	@staticmethod
	def add(bin1, bin2) : 
		'''
		:expects:
			two Binary instances
		:returns:
			a new Binary instance with value equal to the result
			of "bitwise AND" of the two Binary instances
		'''
		pass


# def get_fraction(num) : 
# 	if type(num) == int : 
# 		return float(0)
# 	float_num = num - int(num)
# 	number_of_fraction_digits = len(str(float_num).split('.')[-1])
# 	if float_num > 0 : 
# 		return float(str(float_num)[:number_of_fraction_digits+2])
# 	else : 
# 		return float(str(float_num)[1:number_of_fraction_digits+3])

# i = -1000000000;
# j = i
# while i <  -j: 
# 	if i%100000 == 0 : 
# 		print(i)
# 	if get_fraction(i + 0.23) == 0.0 : 
# 		print('-------- ' + str(i))
# 		break
# 	i += 1
# def get_string_representation_for_float(num) :
# 		'''
# 		:returns:
# 			string decimal representation for the floating point number 'num'
			
# 		##############################
# 		# test cases
# 		##############################
# 		1.23654233 				=> 	'1.23654233'
# 		10000000000000.23654233 => 	'10000000000000.0'
# 		1e-29					=> 	'0.00000000000000000000000000001'
# 		1e29 					=> 	'100000000000000000000000000000.0'
# 		'''

# 		print(num)
# 		if 'e' in str(num) : 
# 			# scientific notation
# 			significand, exponent = str(num).split('e')
# 			if '.' not in significand : 
# 				significand += '.0'
# 			exponent = int(exponent) 
# 			length = 0
# 			if exponent < 0 : 
# 				length = len(significand.split('.')[-1]) + abs(exponent)
# 				return format(num, '.' + str(length) + 'f')
# 			else : 
# 				integer = ''
# 				for element in significand : 
# 					if element != '.' : 
# 						integer += element
# 				print('integer - ' + integer)
# 				if exponent >= len(significand.split('.')[-1]) : 					
# 					return integer + '0'*(exponent - len(significand.split('.')[-1])) + '.0'
# 				else : 
# 					decimal_position = len(significand.split('.')[0]) + exponent
# 					integer = integer[:decimal_position] + '.' + integer[decimal_position:]

# 		else : 
# 			# decimal notation
# 			return str(num)

