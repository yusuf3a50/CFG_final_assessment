"""
Algorithms 1 Solution
-------------------------------------------------------------------------------------------------------------------------
"""
# def isValidSubsequence(array, sequence):
#     pass

# Some test cases are included in order to help you test your solution
# Please note that these are not exhaustive - more will be used during marking, these are only a select few given to help you
# As a result, make sure to think up some on your own and test your code as well!

# Sample Tests for Algorithms 1
# ---------------------------------------------------------

"""
def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)


array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]
print(isValidSubsequence(array1, sequence1))  # FALSE

array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]
print(isValidSubsequence(array2, sequence2))  # TRUE

array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]
print(isValidSubsequence(array3, sequence3))  # TRUE

array3 = [9809823,20980803,8989898,-209802,-19898,0,980980,10]
sequence3 = [-209802, 0, 10]
print(isValidSubsequence(array3, sequence3))  # TRUE

"""



# Python code
# To find the largest number in a list
 
def maxelement(lst):
  # displaying largest element
  # one line solution
  print(max(lst))
 
# driver code
# input list
lst = [20, 10, 20, 4, 100]
# the above input can also be given as
# lst = list(map(int, input().split()))  # -> taking input from the user
# i = 0
# while i < 3:
#     threeMax = []
#     print(lst)
#     print(max(lst))
#     M=max(lst)
#     threeMax.append(M)
#     print(threeMax)
#     lst.remove(max(lst))
#     print(threeMax)
#     i += 1
# print(threeMax)

# Code Analysis
#==============
# The time complexity of this solution is O(n) time, linear, where n is the length of the array.
# The space complexity of this solution is O(1) space, constant.



"""
Algorithms 2 Solution
-------------------------------------------------------------------------------------------------------------------------
"""

"""
def findThreeLargestNumbers(array):
    pass

# Some test cases are included in order to help you test your solution
# Please note that these are not exhaustive - more will be used during marking, these are only a select few given to help you
# As a result, make sure to think up some on your own and test your code as well!

# Sample Tests for Algorithms 2
# ---------------------------------------------------------
array1 = [141, 1, 17, -17, -27, 18, 541, 8, 7, 7]
expectedOutput1 = [18, 141, 541]
print(str(findThreeLargestNumbers(array1)) + " <-- --> " + str(expectedOutput1))  # [18, 141, 541]

array2 = [141, 1, 214, -17, -27, 0, 541, 21, 7, 34]
expectedOutput2 = [141, 214, 541]
print(str(findThreeLargestNumbers(array2)) + " <-- --> " + str(expectedOutput2))  # [141, 214, 541]
"""
array = [20, 10, 20, 4, 100, 589, 3333839893, 38383838, 1000,1,1,1,1,1,1,1,1,1,1,1,1]



def findThreeLargestNumbers(array):
    threeMax = [array[0], array[1], array[2]]
    threeMax.sort()
    for i in range(3, len(array)):
        if array[i] >= threeMax[2]:
            threeMax.append(array[i])
            # print(f"1. after append, threeMax is currently at: {threeMax}")
            threeMax.remove(threeMax[0])
            # print(f"1. after remove, threeMax is currently at: {threeMax}")
        elif array[i] >= threeMax[1]:
            threeMax.insert(2, array[i])
            # print(f"2. after insert, threeMax is currently at: {threeMax}")
            threeMax.remove(threeMax[0])
            # print(f"2. after remove, threeMax is currently at: {threeMax}")
        elif array[i] > threeMax[0]:
            threeMax[0] = array[i]
        #    print(f"3. after reassign, threeMax is currently at: {threeMax}")
        #    print(f"3. after remove, threeMax is currently at: {threeMax}")
    print(threeMax)

findThreeLargestNumbers(array)

# Code Analysis
#==============
# there are simpler ways of coding this but in terms of time complexity, 
# this is the simplest one I found  with a maximum linear time complexity 
# of O(3n-3)+c where:
#       3n is the three conditions that all iterated elements in the list might 
#           have to be tested by
#       n-3 is the length of the list minus the first three values
            # because it is not necessary to iterate through them as they 
            # are immediately assigned to the threeMax list and
#       c is the time complexity of the sort function in threeMax.sort()

# it has a constant space complexity if O(1)









