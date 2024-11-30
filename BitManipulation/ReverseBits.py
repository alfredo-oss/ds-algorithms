"""
If you subtract the last 1 bit reference to 32, you can get how many times you have to shift the binary representation to the right.
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        bit = 0
        res = 0
        for i in range(32): # with this loop i have access to all the elements
            bit = (n >> i) & 1
            res = (bit << (31 - i)) | res # the OR operation is necessary to keep track of the already placed binary elements
        return res