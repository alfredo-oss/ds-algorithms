from typing import List

"""
 The only difference when doing a search range is that the Binary Search is not done on 
 a specific target but a pre-defined range.
"""

# low = 1, high = 100

"""
The definition of "isCorrect" is completely arbitrary.
"""
def isCorrect(n):
    if n > 10:
        return 1
    elif n < 10:
        return -1
    else:
        return 0

def binarySearch(low, high):
    
    while low <= high:
        mid = (low + high) // 2

        if isCorrect(mid) > 0:
            high = mid - 1
        elif isCorrect(mid) < 0:
            low = mid + 1
        else:
            return mid
        
    return -1

