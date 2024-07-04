from typing import List
# Definition of a pair
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def KPInsertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        iter = []
        for i in range(len(pairs)):
            j = 0
            while j >=0 and pairs[j+1][0] < pairs[j][0]:
                temp = pairs[j+1] 
                pairs[j+1] = pairs[j]
                pairs[j] = temp
                iter.append(pairs)
                j-=1
            
            return iter

