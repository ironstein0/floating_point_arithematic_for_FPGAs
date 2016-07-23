# class A(object) : 
	
# 	def __init__(self, param) : 
# 		print('A.__init__ called')
# 		self.param = param

# 	def __new__(cls, param) :
# 		print('A.__new__ called') 
# 		x = object.__new__(cls)
# 		x._initialize(param)
# 		return x

# 	def _initialize(self, param) : 
# 		print('A.__initialize__ called')
# 		self.param = param

# class C(object) : 
# 	def __new__(self, param) : 
# 		print('C.__new__ called')

# class B(C, A) : 

# 	def __init__(self, different_param) : 
# 		print('B.__init__ called')

# 	def __new__(cls, different_param) : 
# 		print('B.__new__ called') 
# 		# x = object.__new__(B)
# 		# param = x.convert_param(different_param)
# 		print(B.__mro__)
# 		x = super(B, cls).__new__(cls, different_param)
# 		return x
# 		# call __new__ of class A, passing "param" as parameter

# 	@staticmethod
# 	def convert_param(param) : 
# 		return param 

# b = B(34)
# b.param

# class A(object):
#     def __init__(self):
#         print "A"
#         super(A, self).__init__()

# class B(object):
#     def __init__(self):
#         print "B"
#         super(B, self).__init__()

# class C(A):
#     def __init__(self, arg):
#         print "C","arg=",arg
#         super(C, self).__init__()

# class D(B):
#     def __init__(self, arg):
#         print "D", "arg=",arg
#         super(D, self).__init__()

# class E(C,D):
#     def __init__(self, arg):
#         print "E", "arg=",arg
#         super(E, self).__init__(arg)

# print "MRO:", [x.__name__ for x in E.__mro__]
# E(10)

# class A(object):
# 	def foo(self):
#    		print('A.foo')
#     	# self.a = 'a'

# class B(A):
# 	def foo(self):
#    		print('B.foo')
#     	super(self.__class__, self).foo(self)

# class C(B):
# 	def foo(self) : 
#    		print('C.foo')
#     	super(self.__class__, self).foo(self)

# c = C()

# class A(object) : 
# 	def foo(self) : 
# 		print('A.foo')
# 		print(self)
# 		self.a = 'a'

# class B(A) : 
# 	def foo(self) : 
# 		print('B.foo')
# 		print(self)
# 		super(self.__class__, self).foo()

# class C(B) : 
# 	def foo(self) : 
# 		print('C.foo')
# 		super(B, self).foo()

# c = C()
# c.foo()

class A(object) : 
	def __new__(cls) : 
		super(B,B).__new__(cls)

class B(A) : 
	def __new__(cls) : 
		print('B.__new__')
		print('cls : ' + str(cls))
		super(B, cls).__new__(cls)

A()