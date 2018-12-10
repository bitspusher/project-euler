from math import sqrt, ceil
primes = list()

def populateListOfInitialPrimes(emptyListOfPrimes):
    emptyListOfPrimes.append(2)
    emptyListOfPrimes.append(3)
    emptyListOfPrimes.append(5)
    emptyListOfPrimes.append(7)
    
def isPrime(num, listOfPrimes):
    maxPrime = int(ceil(sqrt(abs(num))))

    if num == 1 or num == 0:
        return False
    
    for i in listOfPrimes:
        if i > maxPrime:
            return True
        if(num % i == 0):
            if num == i:
                return True
            else:
                return False
    return True

def isTruncatablePrime(num, listOfPrimes):
    #Before shifting, check if the input number is prime
    if(isPrime(num, listOfPrimes) == False):
        return False

    numDigits = 0
    temp = num
    #Right shift
    while(temp > 0):
        
        #keep count of digits, to be used later
        numDigits = numDigits + 1
        
        if(isPrime(temp, listOfPrimes) == False):
            return False
        
        temp = int(temp / 10)
        
    print("Found a left to right shift truncatable prime: " + str(num))
    #Left shift

    divisor = 10 ** (numDigits-1)
    temp = num %(divisor)

    while(temp > 0):
        if(isPrime(temp, listOfPrimes) == False):
            return False
        divisor = divisor / 10
        temp = num % (divisor)
    print("Found a right to left shift truncatable prime: " + str(num))
    return True


