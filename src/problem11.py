def str2int(myStr):
	myIntList = []
	myInt = 0
	for i in range(len(myStr)):
		if myStr[i]!= ' ' and myStr[i]!='\n':
			myInt = int(myStr[i])+myInt*10
		else:
			myIntList.append(myInt)
			myInt = 0
	myIntList.append(myInt)
	print "Integer List="+str(myIntList)
	return myIntList

def gridProd(myIntList, seqLen, size):
    maxProd = 0
    prod = 1
    for i in range(size*size):
    #Up
        for j in range(seqLen):
            if ( i -size*j >= 0) and (i%size == i-size*j % size):
                prod = myIntList[i-size*j]*prod
            else:
                break
        if (prod > maxProd):
            maxProd = prod
        prod = 1
    #Down
        for j in range(seqLen):
            if(i+size*j < size*size) and (i%size == i+size*j % size):
                prod = myIntList[i+size*j]*prod
            else:
                break
        if (prod > maxProd):
            maxProd = prod
    #Right
        prod = 1
        for j in range(seqLen):
            if(i+j < size*size) and (i%size <= (i+j) % size):
                prod = myIntList[i+j]*prod
            else:
                break
        if (prod > maxProd):
            maxProd = prod
        prod = 1
    #Left
        for j in range(seqLen):
            if(i - j >=0) and (i%size >= (i-j)%size):
                prod = myIntList[i-j]*prod
            else:
                break
        if (prod > maxProd):
            maxProd = prod
        prod = 1
    #Diagonal Right Down
        for j in range(seqLen):
            if(((i + size*j + j)<size*size) and (i%size <= (i+size*j+j)%size)):
                prod = myIntList[i+ size*j + j]*prod
            else:
                break
        if (prod >maxProd):
            maxProd = prod
        if prod == 1788696:
            print "Found it!!"
        prod = 1
    #Diagonal Left Down
        for j in range(seqLen):
            if(((i + size*j - j)<size*size) and (i%size >= (i+size*j-j)%size)):
                prod = myIntList[i+ size*j - j]*prod
            else:
                break
        if (prod >maxProd):
            maxProd = prod
        prod = 1

    print " Max Product =" + str(maxProd)

def lp(myStr,seqLen,size):
    gridProd(str2int(myStr),seqLen,size)
	
