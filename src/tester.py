from problem14 import *
from problem15 import *
from problem17 import *
from problem18 import *
from problem21 import *
from problem23 import *
from problem27 import *
from problem12 import *
from problem30 import *
from problem34 import *
from problem35 import *
from problem36 import *
from problem37 import *
from problem41 import *

# The solved Project Euler problems that will be tested by this module
eulerProbNumbers  = [12, 14, 15, 17, 18, 21, 23, 27, 30, 34, 35, 36, 37, 41]

# Arguments to the problem-specific API. "None" if the API does not take arguments
eulerProbArgument = [None,    # Prob. 12
                     999999,  # Prob. 14
                     21,      # Prob. 15
                     1000,    # Prob. 17
                     "../testFiles/prob18Data.txt", # Prob. 18
                     10000,   # Prob. 21
                     28123,   # Prob. 23
                     None,    # Prob. 27
                     5,       # Prob. 30
                     None,    # Prob. 34
                     1000000, # Prob. 35
                     1000000, # Prob. 36
                     None,    # Prob. 37
                     None,    # Prob. 41
                     "../testFiles/prob67Data.txt",    # Prob. 67
                     
# The expected result (return value) for a problem.
sol = [76576500, # Prob. 12
       837799,   # Prob. 14
       137846528820, # Prob. 15
       21124,   # Prob. 17
       1074,    # Prob. 18
       31626,   # Prob. 21
       4179871, # Prob. 23
      -59231,   # Prob. 27
       443839,  # Prob. 30
       40730,   # Prob. 34
       55,      # Prob. 35
       872187,  # Prob. 36
       748317,  # Prob. 37
       7652413, # Prob. 41
       7273,    # Prob 67
      ]
      
def runTests():
    testIdx = 0
    
    for probNum in eulerProbNumbers:
        funcName = "problem" + str(probNum)
        if(eulerProbArgument[testIdx] == None):
            assert globals()[funcName]() == sol[testIdx]
        else:
            assert globals()[funcName](eulerProbArgument[testIdx]) == sol[testIdx]
        
        print "problem" + str(probNum) + " test passed."
        testIdx = testIdx + 1
        
    print "All tests passed successfully"

def main():
    #Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers
    runTests() 
    
if __name__ == "__main__":
    main()