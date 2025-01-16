"""
input: list[int]
output: list[int]

notes:
------
you are given an integer array:
nums = [1,2,4,6] -> total product = 48
prefix = [1 , 2, 8, 48]
suffix = [6, 24, 48, 48]
and you need to return the array that contains the product of all elements BUT
product[i].
    -> which would look something like this:
        Output: [48, 24, 12, 8]
I'm wondering now, what is the pattern that i need to follow. i do understand what needs to be done to get the output.
-> We did the prework of calculating the prefix and suffix(postfix).
               
               prefix = [1 , 2, 8, 48]
               suffix = [6, 24, 48, 48]

               (0) (1)  (2)  (3)
    nums:      [1,  2,   4,   6]
                |              
              [idx]

-> At a given idx in the array. The logic that will give us the product of the remaining elements is:
    prefix[idx - 1] * suffix[idx + 1]
-> A problem can arise when referencing the (-1) and (+1) indexes. Which can be solved by referencing in the inverse way in the creation
   of postfix and suffix.

        # postfix and suffix creation
        ------------------------------
        postfix = [1] * (len(nums) + 1)
        suffix = [1] * (len(nums) + 1)
        n = (len(nums))
        for i in range(len(nums)):
            postfix[i + 1] *= nums[i] * postfix[i - 1]
            suffix[i] *= nums[n] * suffix[n]
            n -= 1
        
-> Once the pre-work is done, we can proceed to calculate the result:

        # result calculation
        --------------------
        for i in range(len(nums)):
            res[i] = postfix[i] * suffix[i + 1]
        return res

-> Here is worth noting that postfix[i] will be always referencing the previous prefix product,
   because that array has 1 more element, thus, the 0-index reference returns the previous value.     

-> In order to avoid confusion is better to isolate the creation of each prefix and suffix.
"""
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        prefix = [1] * (len(nums) + 1)
        suffix = [1] * (len(nums) + 1)
        n = len(nums) - 1
        for i in range(len(nums)):
            prefix[i + 1] *= nums[i] * prefix[i]

        for i in range(len(nums) - 1, -1, -1):
            suffix[i] *= nums[i] * suffix[i + 1]

        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i + 1])
        return res
        