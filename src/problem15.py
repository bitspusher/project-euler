def detectPathsToCorner(i,j, k, l):
    if(i == k) and (j == l):
        global numPathsFound
        numPathsFound = numPathsFound + 1
    if(i < k ):
        detectPathsToCorner(i + 1, j, k , l)
    if(j < l):
        detectPathsToCorner(i, j + 1, k, l)

def detectPathsToCorner2(k, l):
    paths = []
    for i in range(0,k):
        paths.append([])
        for j in range(0,l):
            paths[i].append(0)

    for i in range(0,k):
        for j in range(0,l):
            if(i == 0) and (j == 0):
                paths[i][j] = 1
                continue
            if(j == 0):
                paths[i][j] = paths[i-1][j]
                continue
            if(i == 0):
                paths[i][j] = paths[i][j-1]
                continue
            paths[i][j] = paths[i-1][j] + paths[i][j-1]
    #print("Paths from 0,0 to "+str(k) + "," +str(l) +"="+ str(paths[k-1][l-1]))
    return paths[k-1][l-1]

def problem15(dimSize):
    numPathsFound = 0
    return detectPathsToCorner2(dimSize,dimSize)
