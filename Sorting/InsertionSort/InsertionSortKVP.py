from typing import List
# Definition of a pair
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def KPInsertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        iter = []

        for i in range(n):
            j = i - 1 # The very first element [0] does not enter the iteration because j = -1, hence it does not meet the condition of j >= 0.
            while j >=0 and pairs[j+1].key < pairs[j].key:
                temp = pairs[j+1] 
                pairs[j+1] = pairs[j]
                pairs[j] = temp
                j-=1
            iter.append(pairs) # Iter appending goes here because this is the step after which every comparison for the observed elment has already been done.
     
        return iter

