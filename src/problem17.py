
def intToLetters(i):
	numDigits = len(str(i))
	stringsOfNumbers = dict()
	stringsOfNumbers[1]  = "one"
	stringsOfNumbers[2]  = 'two' 
	stringsOfNumbers[3]  = 'three'
	stringsOfNumbers[4]  = 'four'
	stringsOfNumbers[5]  = 'five'
	stringsOfNumbers[6]  = 'six'
	stringsOfNumbers[7]  = 'seven'
	stringsOfNumbers[8]  = 'eight'
	stringsOfNumbers[9]  = 'nine'
	stringsOfNumbers[10] = 'ten'
	stringsOfNumbers[11] = 'eleven'
	stringsOfNumbers[12] = 'twelve' 
	stringsOfNumbers[13] = 'thirteen'
	stringsOfNumbers[14] = 'fourteen'
	stringsOfNumbers[15] = 'fifteen' 
	stringsOfNumbers[16] = 'sixteen' 
	stringsOfNumbers[17] = 'seventeen' 
	stringsOfNumbers[18] = 'eighteen' 
	stringsOfNumbers[19] = 'nineteen' 
	stringsOfNumbers[20] = 'twenty' 
	stringsOfNumbers[30] = 'thirty'
	stringsOfNumbers[40] = 'forty' 
	stringsOfNumbers[50] = 'fifty'
	stringsOfNumbers[60] = 'sixty'
	stringsOfNumbers[70] = 'seventy'
	stringsOfNumbers[80] = 'eighty'
	stringsOfNumbers[90] = 'ninety'
	string=''
	while(i):
		if(int(i/1000)):
			string = string + stringsOfNumbers[int(i/1000)]
			string = string+"thousand"
			if(i%1000 != 0):
				string = string + "and"
			i = i % 1000
		elif(int(i/100)):
			string = string + stringsOfNumbers[int(i/100)]
			string=string + "hundred"
			if(i%100 != 0):
				string = string + "and"
			i = i%100
		elif(int(i/10)):
			if(i >= 10) and (i <=19):
				string = string+stringsOfNumbers[i]
				i = 0
			else:
				string=string+stringsOfNumbers[int(i/10)*10]
			i = i % 10
		else:
			string=string+stringsOfNumbers[i]
			i = 0
		
	print(str(string))
	return string
    
def numberLetterCounts(n):
	letterCount = 0
	for i in range(1,n+1):
		letterCount = letterCount + len(intToLetters(i))
	#print("Length of strings from 1 through 1000 = "+ str(letterCount))
	return letterCount
    
def problem17(count):
	return numberLetterCounts(count)