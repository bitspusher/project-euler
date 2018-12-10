def ami(endNum):
    import math
    factors = set()
    factors2 = set()
    amicable = set()
    for i in range(2,endNum):
        sumFac = 0
        sumFac2 = 0
        factors.clear()
        factors2.clear()
        for j in range(2,int(math.sqrt(i))+1):
            if i%j == 0:
                factors.add(j)
                factors.add(i/j)
        factors.add(1)
        for j in factors:
            sumFac = sumFac + j
        
        for j in range(2,int(math.sqrt(sumFac))+1):
            if sumFac%j == 0:
                factors2.add(j)
                factors2.add(sumFac/j)
        factors2.add(1)
        for j in factors2:
            sumFac2 = sumFac2 + j
        if (i == sumFac2 )and i != sumFac:
            #print "Amicable Numbers Found!"
            #print str(i) + " " + str(sumFac)
            amicable.add(i)
            amicable.add(sumFac)
    totalSum = 0
    for j in amicable:
        totalSum = totalSum + j
    #print "Sum of all amicable numbers is "+str(totalSum)
    return totalSum

def problem21(upperLimit):
    return ami(upperLimit)   
    
        
