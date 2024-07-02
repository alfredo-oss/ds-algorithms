class Solution:
    def insertionSort(arr):
        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):
            j = i - 1
            while j >= 0  and arr[j+1] < arr[j]:
                # Since we passed the condition the bucle will be executed (Condition: arr[j] and arr[j+1] are out of order)
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp
                j-=1 # we have to decrease since we are comparing the elements while going backwards
            return arr