
factorials = []
def fact(num):
	factorial = 1
	while(num != 0):
		factorial = num * factorial
		num = num - 1
	return factorial

def getSumOfFactorialOfDigits(num):
	global factorials
	sumOfFactorialOfDigits = 0
	for i in str(num):
		sumOfFactorialOfDigits = sumOfFactorialOfDigits + factorials[int(i)]
	#print("Sum of the factorial of the digits = "+ str( sumOfFactorialOfDigits))
	return sumOfFactorialOfDigits

def problem34():
	global factorials
	for i in range(0,10):
		factorials.append(fact(i))
	sumOfNumbersEqualToSumOfFactorialOfTheirDigits = 0 

	upperLimit = 9
	while(getSumOfFactorialOfDigits(upperLimit) > upperLimit):
		upperLimit = upperLimit * 10 + 9
	for i in range(3, upperLimit):
		if getSumOfFactorialOfDigits(i) == i:
			sumOfNumbersEqualToSumOfFactorialOfTheirDigits = sumOfNumbersEqualToSumOfFactorialOfTheirDigits + i
	print("Sum of numbers that are also the sum of the factorials of their digits = "+ str(sumOfNumbersEqualToSumOfFactorialOfTheirDigits))
	return sumOfNumbersEqualToSumOfFactorialOfTheirDigits
