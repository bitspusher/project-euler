def getSumOfDigits(numStr, power):	
	sum = 0
	for i in numStr:
		sum = sum + int(i) ** power
	return sum

def isASumOfPowerOfDigits(num, power):
	#COnvert to string and then extract digits
	numStr = str(num)
	sum = getSumOfDigits(numStr, power)
	
	if(sum == num):
		print(str(sum))
		return True
	else:
		return False

def numSumOfPowers(power):
	numCount = 0
	sumOfNumbers = 0
	curNum = 10
	upperLimit = getSumOfDigits(str(99999), power)
	#for i in range(10,100000):
		#Check if a number is also the sum of the specified powers of its digits
	#for i in range(10,10**power):
	while(curNum <= upperLimit):
		if (isASumOfPowerOfDigits(curNum, power)):
			sumOfNumbers = sumOfNumbers+curNum
			numCount = numCount+1
		curNum = curNum + 1

	#print(str(numCount) + " numbers can be expressed as a sum of the " +str(power)+"th power of their digits")
	#print("The sum of numbers is "+str(sumOfNumbers))
	return (sumOfNumbers)

def problem30(power):
	return numSumOfPowers(power)