from prime import *

primes = list()

def genPrimesInRange(start, end):
    for i in range(start, end):
        if(isPrime(i, primes)):
           primes.append(i)

def printPrimes(pList):
    for i in pList:
           print(str(i))
           
def problem27():
    populateListOfInitialPrimes(primes)
    genPrimesInRange(2, 10000)
    #printPrimes(primes)
    n = 0
    maxNumConsecutivePrimes = 0
    coefficientProd = 0.0
    coefficientRange = 1000
    for a in range(-coefficientRange, coefficientRange, 1):
        for b in range(-coefficientRange, coefficientRange, 1):
            n = 0
            while(isPrime(n * (n +a) + b, primes)):
                  n = n + 1
            if n > maxNumConsecutivePrimes:
                  maxNumConsecutivePrimes = n
                  coefficientProd = a * b
    print ("The max number of consecutive primes is " + str(maxNumConsecutivePrimes))
    print ("Product of the coefficients is " + str(coefficientProd))
    return coefficientProd