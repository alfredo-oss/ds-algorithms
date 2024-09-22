from typing import List
from collections import deque

class Solution:
    def Subset(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = deque(nums)

        def backtrack(temp):

            print(temp)
            res.append(list(temp))

            if not temp:
                return res
            
            if [temp[0]] not in res:
                res.append([temp[0]])
                
            temp.popleft()
            backtrack(temp)

        backtrack(temp)
        return res
    
solution = Solution()
test = [1,2,3]
result = solution.Subset(test)
print(result)