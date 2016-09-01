def reciprocal(x, numberOfIterations) : 
	returnValue = 0
	for i in range(numberOfIterations) : 
		print('i : ' + str(i))
		t1 = (-1)**i
		t2 = (x-1)**i
		print('t1 : ' + str(t1))
		print('t2 : ' + str(t2))
		returnValue += t1*t2
		print(returnValue)
	return returnValue

def reciprocal_modified(x, x_approx, numberOfIterations) :
	sum_ = 0
	for i in range(numberOfIterations) : 
		t1 = (-1)**i
		t2 = (x*x_approx - 1)**i
		sum_ += t1*t2
		print('t1 : ' + str(t1))
		print('t2 : ' + str(t2))
		print('t1*t2 : ' + str(t1*t2))
	return sum_

print(reciprocal_modified(1.5, 1.5, 100))
