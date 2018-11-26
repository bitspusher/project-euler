def collatz(startNum):
    n = startNum
    collatzSeq = []
    while(n!=1):
        collatzSeq.append(n)
        if (n%2 == 0 ):
            n = n/2
        else:
            n = 3*n + 1
    collatzSeq.append(n)
    #print "Collatz Sequence = "+str(collatzSeq)
    return len(collatzSeq)

def maxColSeqLen(num):
    startNum = 0
    maxLen = 0
    while(num>0):
        length = collatz(num)
        if ((length)>maxLen):
            maxLen = length
            startNum = num
        num = num -1
    #print "Max start num ="+str(startNum)
    #print " Length of longest sequence="+str(maxLen)
    return startNum
    
def problem14(input):
    return maxColSeqLen(input)

        
            
