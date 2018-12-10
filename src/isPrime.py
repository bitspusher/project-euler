primes = list()

def isPrime(num, listOfPrimes):
    for i in listOfPrimes:
        if(num % listOfPrimes == 0):
            return false
    return true
