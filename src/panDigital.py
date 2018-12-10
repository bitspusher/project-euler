# Hash Table used for quick lookup to see if a digit was
# already found in the number to be checked
digitHashTable = [0,0,0,0,0,0,0,0,0,0]
def isPandigital(num):
    # Clean out hash table
    for i in range(10):
        digitHashTable[i] = 0
    while(num != 0):
        rem = num %10
        if(digitHashTable[rem] != 0):
            return False
        num = int(num / 10)
        digitHashTable[rem] = 1
    return True

#Input to this is assumed to be a pandigital number
def isZerolessPanDigital(num):
    while(num > 0):
        if((num % 10) == 0 ):
            return False
        else:
            num = int(num / 10)
    return True

# Assume input is pan-digital. Looks for 1 to N, so discard numbers with 0 in them.
def isNDigitPanDigital(num):
    numDigits = 0
    #Clean hash table
    for i in range(10):
        digitHashTable[i] = 0
     
     
    while(num != 0):
        i = num % 10
        digitHashTable[i] = 1;
        numDigits = numDigits + 1
        num = int(num / 10)

    #No zeroes allowed in N digit pandigital numbers
    if digitHashTable[0] == 1:
        return False
    
    index = 1
    
    #Now go through the hash table and look for gaps
    while(index <= numDigits):
        if(digitHashTable[index] == 0):
            return False
        index = index + 1
    
    return True

def convNumToListOfDigits(num, arrayOfDigits):
    #print("Converting number:" + str(num) + " to digits")
    
    while(num > 0):
        arrayOfDigits.append(num % 10)
        num = int(num / 10)
        
    #print(" Array of digits --> ")
    #for x in arrayOfDigits:
    #    print(x)
    return len(arrayOfDigits)

# Returns the next highest pandigital number from
# the input number
def nextLowerPanDigitalNum(num):
    num = num -1
    digitArr = []
    numDigits = convNumToListOfDigits(num, digitArr)
    matchFound = False

    temp = num
    while(temp > 0):
        for i in range(numDigits - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if digitArr[i] == digitArr[j]:
                    #Found a match of digits
                    matchFound = True
                    break
            #Break outer for loop as well
            if(matchFound):
                break
            
        if (matchFound == False):
            #print("Didn't find matching digits. Pandigital!\n")
            # Found a pandigital number
            return temp
        else:
            #Continue searching
            #print("Match found\n")
            rem = temp % ( 10 ** (j))      
            temp = temp - (1 + rem)
                
            #print("New intermediate number:" + str(temp) +"remainder subtracted from previous num:" + str(rem))
            
            #Update the string with the new intermediate number
            #Wipe Digit array before populating again
            digitArr[:] = []
            matchFound = False
            numDigits = convNumToListOfDigits(temp, digitArr)
    return temp
    
    
    
