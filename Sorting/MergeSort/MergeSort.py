from typing import List

class CustomSort:
# Implementation of MergeSort

    # Utility function "merge"
    def merge(self, arr: List[int], s: int, m: int, e: int) -> None:

        # Copy the sorted left & right halfs to temp arrays
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        i = 0 # index for L
        j = 0 # index for R
        k = s # index for arr

        # Merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else: 
                arr[k] = R[j]
                j += 1
            k += 1
        
        # One of the halfs will have elements remaining
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


    def mergeSort(self, arr: List[int], s: int, e: int) -> List[int]:
        if e - s + 1 <= 1:
            return arr
        
        # The middle index of the array
        m = (s + e) // 2

        # Sort the left half
        self.mergeSort(arr, s, m)

        # Sort the right half
        self.mergeSort(arr, m + 1, e)

        # Merge the SORTED halfs
        self.merge(arr, s, m, e)                 

        return arr

    