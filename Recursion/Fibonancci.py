"""
Create a function to calculate the nth fibonacci number with two branch recursion.
Fibonacci Number: F(n) = F(n-1) + F(n-2)
Base cases: F(0) = 0, F(1) = 1
"""
class Solution:
    def fibonacci(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fibonacci(n-1) + self.fibonacci(n-2)