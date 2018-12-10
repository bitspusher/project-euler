from math import ceil

def isPalindromeDec(decNum):
	decStr = str(decNum)
	i = 0
	j = len(decStr) - 1

	while(i < j):
		if decStr[i] == decStr[j]:
			i = i + 1
			j = j - 1
			continue
		return False
	return True

def isPalindromeBin(binStr):
	i = 0 
	j = len(binStr) - 1

	while(i < j):
		if binStr[i] == binStr[j]:
			i = i + 1
			j = j - 1
			continue
		return False

	return True
	
def decNumberToBinStr(decNum):
	binStr=""
	while(decNum != 0):
		if(decNum % 2 == 0):
			binStr = ''.join(('0', binStr))
		else:
			binStr = ''.join(('1', binStr))
		decNum = int(decNum/2)
	return binStr

def checkIfDecAndBinPalindrome(num):
	if(isPalindromeDec(num)):
		if(isPalindromeBin(decNumberToBinStr(num))):
			return True
	return False

def problem36(upperLimit):
	sumOfPalindromes = 0
    
	for i in range(1, upperLimit+1):
		if checkIfDecAndBinPalindrome(i):
			#print(str(i))
			sumOfPalindromes = sumOfPalindromes + i
	#print("Sum of binary and decimal palindromes below " + str(upperLimit) + " is " + str(sumOfPalindromes))  
	return sumOfPalindromes
