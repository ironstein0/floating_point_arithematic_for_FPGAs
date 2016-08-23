import sys
import random
import matplotlib.pyplot as plt

sys.path.insert(0, '..')
from src.IterativeLogarithmicMultiplier import FixedWidthIntegerMultiplier

iterationsPerCorrectionIteration = 1000

numberOfInputBits = 53
minValue = int('1' + '0'*(numberOfInputBits-1), base=2)
maxValue = int('1'*numberOfInputBits, base=2)
print('mininum {0} bit value : '.format(numberOfInputBits) + str(minValue))
print('maximum {0} bit value : '.format(numberOfInputBits) + str(maxValue))

def mod(n) : 
	if n < 0 : 
		return -n 
	return n

def error_vs_correctionIterations() : 	

	relativeErrorSumList = []
	correctionIterationsList = []
	numIncorrectList = []
	for i in range(1, numberOfInputBits+1) : 
		correctionIterationsList.append(i)

	for correctionIterations in range(1, numberOfInputBits+1) : 
		multiplier = FixedWidthIntegerMultiplier(numberOfInputBits, numberOfInputBits*2, correctionIterations)

		print('correctionIterations : ' + str(correctionIterations))
		relativeErrorSum = 0	
		numIncorrect = 0
		for i in range(iterationsPerCorrectionIteration) : 
			n1 = random.randint(minValue, maxValue)
			n2 = random.randint(minValue, maxValue)
			
			result_reqd = n1*n2
			result_getd = int(multiplier.multiply(bin(n1)[2:], bin(n2)[2:]), base=2)

			relativeErrorSum += mod(result_reqd - result_getd)*1.0/result_reqd

			if relativeErrorSum != 0 : 
				numIncorrect += 1

		relativeErrorSumList.append(relativeErrorSum/iterationsPerCorrectionIteration)
		numIncorrectList.append(numIncorrect)

	print(relativeErrorSumList)
	print(correctionIterationsList)
	plt.xticks([1, 2, 3, 4, 5])
	plt.subplot(121)
	plt.plot(correctionIterationsList, relativeErrorSumList)
	plt.subplot(122)
	plt.plot(correctionIterationsList, numIncorrectList)
	plt.show()


error_vs_correctionIterations()