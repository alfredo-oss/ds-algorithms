"""
Given an array of values, design a data structure that can query the sum of
a sub array of the values.
notes:
-----
* when asked for designing a data structure, you actually 
  need to design a place to store data an which has certain
  behavior.
* in this case, we are asked to design a method of the data structure
  that is able to return the sum of a sub array, for any two-contiguous 
  points of the array.
* example:
  [2, -1, 3, -3, 4] this is the array we would receive.
  -> when receiving the array we need to initialize the constructor
     of the prefix sum.
  -> once we have the prefix sum we can calculate the queried sum,
     which follows this logic:
     querySum(L, R)
     if L > 0:
        we need to subtract everything that came previous to L.
"""
class prefixSum:
    def __init__(self, arr: list[int]):
        self.prefix = []
        cur = 0
        for n in arr:
            cur += n
            self.prefix.append(cur)
    
    def querySum(self, L, R):
        if L > 0:
            p_sum = self.prefix[R] - self.prefix[L - 1]
        else:
            p_sum = self.prefix[R]
        return p_sum