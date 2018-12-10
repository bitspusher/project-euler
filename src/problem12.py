import math
def numDiv(triNum):
    divisors = 0
    facs=set()
    for i in range(1,int(math.sqrt(triNum))):
        if ( triNum % i == 0 ):
            if i not in facs:
                divisors = divisors + 1
                facs.add(i)
            if (triNum/i) not in facs:
                divisors = divisors + 1
                facs.add(triNum/i)
    return divisors

def problem12():
    num = 1
    index = 1
    while(numDiv(num) < 500):
        index = index + 1
        #print num
        num = index + num
    print num
    return num
        
