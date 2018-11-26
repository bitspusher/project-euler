def problem18(inputFile):
    numbers = []
    numRows = 0
    with open(inputFile) as f:
        for line in f:
            numRows = numRows + 1
            data = line.split()
            for nums in data:
                numbers.append(int(nums))
                #print(str(nums))

    numElementsInRow = 2
    currentElement = 0

    for i in range(1, numRows):
        for j in range(0, numElementsInRow):
            currentElement = currentElement + 1
            if(j == 0):
                numbers[currentElement] = numbers[currentElement - numElementsInRow + 1] + numbers[currentElement]
                continue
            if(j == numElementsInRow-1):
                numbers[currentElement] = numbers[currentElement - numElementsInRow] + numbers[currentElement]
                continue
            if (numbers[currentElement - numElementsInRow + 1] > numbers[currentElement - numElementsInRow]):
                numbers[currentElement] = numbers[currentElement -numElementsInRow + 1] + numbers[currentElement]
            else:
                numbers[currentElement] = numbers[currentElement - numElementsInRow] + numbers[currentElement]
        numElementsInRow = numElementsInRow + 1

    #for nums in numbers:
        #print(str(nums))

    #Find the greatest number in the last row
    currentElement = (int)(((numRows-1) * (numRows))/ 2)
    greatest = 0
    for i in range(currentElement, currentElement + (numElementsInRow - 1)):
        if (greatest < numbers[i]):
            greatest = numbers[i]
    print("The path with the greatest sum has sum = "+str(greatest))
    return greatest