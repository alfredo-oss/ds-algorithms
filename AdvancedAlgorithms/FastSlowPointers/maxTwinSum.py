"""
- My intuition is that we need to return twins as we find them in one pass.
- We know that the length of the linked list is even, but, we don't actually know
  what what the length of the linked list is, so we cant access elements by indexing
  them.
- The twin of an element is given by:
    (n - i - 1) where 0 <= i <= (n / 2 - 1)
- I could "send a pointer" to scan my n. Given that I know my n, I know my limit.
- Then I could shift a slow pointer searching for a twin example i = 0 we know that its twin should be n - i - 1,
  now we can ask the question: 
    -> does n - i - 1 exist? if yes, then we shift our fast pointer as many times as moves = (n - i - 1) - i is.
    -> we perform the sum of values and store it in an array.

Hint (1):
--------
How can reversing part of the linked list help find the answer?
Let's take the case of:

Original: (5) -> (4) -> (2) -> (1)

Reversed: (1) -> (2) -> (4) -> (5)
                  
2nd half]          
* how can I reverse a linked list?
  for every traversed node you need to invert the pointers,
  initializing the first pointer to None, thus, the tail of
  the linked list. 
* now the question is: how do I even get to the second half if I dont know what a half is?
* if there is a half I should be able to reverse it.
I need to use the half because if I use the original Node List I will not be able to compare if the Node
has already been visited since nothing asures me that there are no duplicates.
* My question is: What is the initialization logic?
"""
from typing import Optional
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def pairSum(self, head:Optional[ListNode]) -> int:
        