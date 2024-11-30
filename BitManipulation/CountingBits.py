from typing import List

class Solution:
    def countBits(self, n: int) -> int:
        def helpHammingWeight(n):
            count = 0
            while n > 0:
                if n & 1 == 1:
                    count += 1
                n = n >> 1
            return count
        aux = []
        for element in range(n + 1):
            aux.append(helpHammingWeight(element))
        return aux