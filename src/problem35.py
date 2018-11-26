from math import sqrt


def isPrime(num):
	if(num == 2) or (num == 3):
		return True
	#Don't bother checking even numbers
	if (num & 1) != 1: 
		return False
	
	for i in range(2, int(sqrt(num) + 1)): #most optimal range
		if (num % i == 0 ):
			return False
	return True

def isCircularPrime(inputNum):
	if(inputNum < 10):
		if(isPrime(inputNum)):
			return True
		else:
			return False
	numDigits = len(str(inputNum))
	
	isCircularPrime = True
	numToCheck = inputNum
	numIterations = numDigits
	#Generate all the circular combinations of the input numbers
	while(numIterations):
		if(isPrime(numToCheck)):
			#Rotate
			numToCheck = (numToCheck % (10 ** (numDigits - 1)))* 10 + (int(numToCheck / (10 ** (numDigits - 1)))) 
		else:
			#Not a prime. Return false
			return False
		numIterations = numIterations - 1
	return True

def problem35(upperLimit):
	numberOfCircPrimesFound = 0
	for i in range(2, upperLimit + 1):
		if isCircularPrime(i):
			#print("Found a circular prime! : " + str(i))
			numberOfCircPrimesFound	= numberOfCircPrimesFound + 1
	#print("Number of Circular Primes below " + str(upperLimit) + " " + str(numberOfCircPrimesFound))
	return numberOfCircPrimesFound
