"""
input: Optional[ListNode] # represents the head of a linked list.
output: int

example:
--------
* the twin of a node (i) is defined by:
  (n - 1 - i)th

[5, 4, 2, 1]
 t1 t2 t2 t1

lets analyze how I could achieve this with fast and slow pointers:
------------------------------------------------------------------
- I know that my slow pointer will ALWAYS traverse the half of the array.
  meanwhile I traverse the half of the array I could reverse half of the pointers,
  because that would allow me to do the following:
  initial round:
  (5) -> (4) -> (2) -> (1)
                [s]        [f] # this is where the loop will stop
  None <- (5) <- (4)  (2) -> (1)
               [prev] [s]        # then, we initialize another loop that 
                                   initializes two pointers on both halfs
                                   and starts iterating and returning the 
                                   sum, maximizing it
- Now, how can we actually achieve this:
  slow, fast = head, head
  prev, temp = None, None

  while fast and fast.next:
    fast = fast.next.next  --> [KEY CONCEPT HERE: Since we are mutating the linked list we need to first shift our fast pointer]
    tmp = slow.next # we hold the next node
    slow.next = prev # we re-assign the value of the current pointer, [!!! If we put our fast pointer assignation after this statement we would be shifting it towards a NULL node !!]
    prev = slow # we update the prev value to the current node, because on the next iteration it will become the previous
    slow = tmp # we move on to the next node
    

- since we reversed the first half of the linked list and we hold the prev and s value, we can start our 2nd iteration.
  curSum = 0
  while prev and slow:
    curSum = max(prev.val + slow.val, curSum)
    prev = prev.next
    slow = slow.next
  return curSum
"""
from typing import Optional
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        curSum = 0
        while slow:
            curSum = max(prev.val + slow.val, curSum)
            prev = prev.next
            slow = slow.next
        return curSum