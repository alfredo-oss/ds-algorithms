"""
input: List[int] -> is an array of integers
output: int -> maximum profit

notes:
------
* target time complexity is O(n) and space O(1)
* i know what the brute force solution would be but that is an O(n^2) tc, which is trying for every posible solution.
 -> what I know is that i need the minimum value on the left pointer and the maximum value on the right pointer and then subtract the max - min value.
 -> the left value has to always be behind the right value, at least by a day.

L, R = 0, 1
maxP = 0
while R < len(prices):
    if prices[L] < prices[R]:
        maxP = max(maxP, prices[R] - prices[L])
    else:
        L = R
    R += 1
return maxP
"""