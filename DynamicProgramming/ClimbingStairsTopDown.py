"""
Input: An integer n, representing the number of steps to reach to the
       top of a staircase. Thats the total length of the path.
     - You can either take 1 or 2 steps at the time.

Output: Return the number of distinct ways to climb to the top of
        the staircase.

top down:
         input: 5
              [5]
              /  \
            [4]  [3]  # 10 could be reached from 4 or from 3, since I can take 1 or 2 steps
            / \   /\
         [3]  [2]
         / \   / \
       [2] [1][1] [0]
       / \   \
      [1] [0] [0]
""" 
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def helperTopDown(n, cache):
            if n < 2:
                return 1
            if n in cache:
                return cache[n]
            
            cache[n] = helperTopDown(n-1) + helperTopDown(n-2)
            return cache[n]
        return helperTopDown(n, cache)