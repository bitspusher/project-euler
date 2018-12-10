def perm(listNum):
    perms = set()
    for i in range(len(listNum)):
        for j in range(len(listNum)):
            num = str(listNum[i])
            for k in range(len(listNum)):
                if(i!= (k+j)%len(listNum)):
                    num+=str(listNum[(k+j)%len(listNum)])
            perms.add(num)
    print perms



