import math

def isAbundant(num):
    factors = set()
    for i in range(2,int(math.sqrt(num))+1):
        if ( num % i == 0):
            factors.add(i)
            factors.add(num/i)
    sumFac = 0
    for j in factors:
        sumFac = sumFac + j
    if sumFac >num:
        return True
    else:
        return False

def arrAbundant(limit):
    abundantNums = set()
    for i in range(limit):
        if (isAbundant(i)):
            abundantNums.add(i)
    #print "Abundant Numbers = "+str(abundantNums)
    return abundantNums

def sumAbundants(setIn):
    setOut = set()
    for i in setIn:
        for j in setIn:
            setOut.add(i+j)
    #Return set of numbers that can be expressed as a sum of two abundant numbers
    return setOut

def sumAbundantNums(setIn,limit):
    totalSum = 0
    i=1
    while(i<limit):
        if i not in setIn:
            totalSum = totalSum + i
        i = i+1
    return totalSum

def problem23(limit):
    arrayAbundantSum = set()
    arrayAbundantSum = sumAbundants(arrAbundant(limit))
    #print "Sum of integers that cannot be expressed as a sum of two abundant numbers"
    #print str(sumAbundantNums(arrayAbundantSum,limit))
    return sumAbundantNums(arrayAbundantSum,limit)

