"""
You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return None
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
