"""
input: arr: List[int] (arr where there should be multiple sign flips)
output: res: int (it represents the length of the array where the turbulent condition is met)

notes:
-------
* the array is not circular
* im assuming the description mentions that the comparison flips when the 
  "next" element of the array is greater or smaller than the previous one.
* there has to be some type of boolean pointer keeping track of the "turbulent"
  condition.
* we need to keep track of our currentSum and our maxSum, every time we do not meet the condition
  the currSum needs to be reseted to 0.

solution:
---------
currSum = 0
maxSum = 0
signHelp = [">", "<"]
currSign = ""
prevSign = ""
for i in range(len(arr)):
    curSum += 1
    maxSum = max(curSum, maxSum)
    if arr[i] > arr[i + 1]:
        currSign = signHelp[0]
    elif arr[i] < arr[i + 1]:
        currSign = signHelp[1]
    if currSign == prevSign:
        curSum = 0
    prevSign = currSign
return maxSum 
        
"""
from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        res, prev = 1, ""
        while r < len(arr):
            if arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r = r + 1
                prev = "<"
            elif arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r = r + 1
                prev = ">"
            else:
                r = r + 1 if arr[r - 1] == arr[r] else r
                l = r - 1
                prev = ""
        return res