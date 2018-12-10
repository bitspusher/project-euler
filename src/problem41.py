from prime import *
from panDigital import *
from math import sqrt, ceil
from time import time
primes = list()

def genPrimesInRange(start, end):
    #startTime = time()
    #milUpperBound = 1000000
    #Starting number should be odd, so incrementing in 2s
    for i in range(start, end, 2):
        #if(i > milUpperBound):
        #    print("Time to find primes in this million integer range : " + str(time() - startTime))
        #    milUpperBound = milUpperBound + 1000000
        #    startTime = time()
        if(isPrime(i, primes)):
            primes.append(i)
        
def problem41():
    #Find the largest pandigital prime. Start backwards.
    # The largest pandigital number is 9876543210
    
    lastNum = 9876543211
    
    populateListOfInitialPrimes(primes)
    genPrimesInRange(9, int(ceil(sqrt(lastNum))))

    print("Generated " + str(len(primes)) + "primes")
    #Don't consider even numbers
    n = lastNum - 1
    percent = lastNum / 100
    while n > 0:
        #if(isPandigital(n)):
        n = nextLowerPanDigitalNum(n)
        #print("Testing number " + str(n))

        #We need to find a zero-less pandigital number
        if isNDigitPanDigital(n):
            #Check if prime
            if isPrime(n, primes):
                print("The largest pandigital prime is " + str(n))
                break
        else:
            continue
    return n
    '''
    num = 99234990
    print("Testing lower pan-digital number code\n. Input number is " + str(num))
    
    print("Next lower pan-digital number is " + str(nextLowerPanDigitalNum(num)))

    '''
