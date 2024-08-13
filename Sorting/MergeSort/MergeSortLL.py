from typing import List

class Pair:
    def __init__(self, key: int, value: str) -> None:
        self.key = key
        self.value = value

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)
    
    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:  
        
        if e - s + 1 <= 1:
             return pairs
         
        m = (s + e) // 2

        # Sort the left half
        self.mergeSortHelper(pairs, s, m)

        # Sort the right half
        self.mergeSortHelper(pairs, m+1, e)

        # Merge the two sorted pairs:
        self.merge(pairs, s, m, e)

        return pairs
    
    def merge(self, pairs: List[Pair], s: int, m: int, e: int) -> List[Pair]:
        
        # Creation of the temporary arrays
        ## Left side of the temp array     
        L = pairs[s:m+1]
        R = pairs[m+1:e+1]

        i = 0
        j = 0
        k = s

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j += 1
            k +=1

        # In case of reminiscing elements in either one of the arrays

        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1