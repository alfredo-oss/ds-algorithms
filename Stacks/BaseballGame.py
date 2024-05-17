"""
operations = ['5', '+','D', 'C'] 
The order of the operations would be append(5), append(arr[i-1]+arr[i-2]), append(2*arr[i-1]),pop()
"""
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for operation in operations:
            if operation == '+':
                arr.append(arr[-1]+arr[-2])
            elif operation == 'D':
                arr.append(2*arr[-1])
            elif operation == 'C':
                arr.pop()
            else:
                arr.append(int(operation))
        return sum(arr)
    
solution = Solution()
test_operations = ["5","2","C","D","+"]
res = solution.calPoints(test_operations)
print(res)