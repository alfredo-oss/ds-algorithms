from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs
    
    def quickSortHelper(self, pairs: List[Pair], s: int, e: int) -> None:

        if e - s + 1 <= 1:
            return pairs
        
        pivot = pairs[e]
        left = s

        for i in range(s, e): # It is necessary to add the range "s - e" because s will vary once its called recursively to sort the right's halfs!!
            if pairs[i].key < pivot.key:
                tmp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = tmp
                left += 1

        # Re - assign the pivot to the element where the left pointer kept pointing after the iteration         
        pairs[e] = pairs[left]
        pairs[left] = pivot 

        # Recursive call on the remaining left part of the array
        self.quickSortHelper(pairs, s, left - 1)

         # Recursive call on the remaining right part of the array
        self.quickSortHelper(pairs, left + 1, e)
