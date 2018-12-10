from prime import *
from panDigital import *

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
            
def problem37():
    remTruncatablePrimes = 11
    sumOfTruncatablePrimes = 0
    num = 11
    
    populateListOfInitialPrimes(primes)
    genPrimesInRange(9, 1000000)
    #print("Generated primes in range 2- 10000")

    while remTruncatablePrimes > 0:
    
        if(isTruncatablePrime(num, primes)):
            #print ("Found a truncatable prime:" + str(num) )
            sumOfTruncatablePrimes = sumOfTruncatablePrimes + num
            remTruncatablePrimes = remTruncatablePrimes - 1
        
        num = num + 1
    
    print("Sum of truncatable primes:" + str(sumOfTruncatablePrimes))
    return sumOfTruncatablePrimes
