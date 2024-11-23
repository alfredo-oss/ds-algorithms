class Solution:
    def climbStairs(self, n: int):
        if n <= 2:
            return n
        dp = [1,2]
        i = 3
        while i <= n:
            tmp = dp[1]
            dp[1] = dp[1] + dp[0]
            dp[0] = tmp
            i += 1
        return dp[1]
    