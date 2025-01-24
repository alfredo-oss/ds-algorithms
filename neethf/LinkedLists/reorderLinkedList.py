"""
input: Optional[ListNode] # head of a Linked List
output: Optional[ListNode] # a reordered Linked List

notes:
------
* the positions of a linked list of length 7 can be represented:
    (0) -> (1) -> (2) -> (3) -> (4) -> (5) -> (6)

* the re-ordering of nodes would look like:
    (0) -> (6) -> (1) -> (5) -> (2) -> (4) -> (3)
    [0]   [n-1]   [1]   [n-2]   [2]   [n-3]   [3]

how can we achieve this re-order?
---------------------------------
* I need to have access to all the n-x elements, thus, need to 
  traverse the entire array.
* the direction of the list needs to be maitained.
* I think what makes the most sense is to invert the second half of the list.
* Lets proceed with that approach.

1st loop: [pointers are initialized to the half and end of the array]

(0) -> (1) -> (2) -> (3) -> (4) -> (5) -> (6) 
                      s                    f
* this is easy to achieve in one pass O(n)

2nd loop:
                     [slow pointer needs 
                      to start here]        
                             |  
(0) -> (1) -> (2) -> (3) <- (4) <- (5) <- (6)
* the concept is right but this has to be divided into two different lists,
  otherwise an infinite loop is created. 
                                           s
to achieve this we start our slow pointer and start
reversing the remaining half of the array O(n/2)

3rd loop:
(0) -> (6) -> (1) -> (5) -> (2) -> (4) -> (3)
to achieve this we will start a poiter at the head of 
the list and we will take the last s pointer of the 
previous reversing loop and start switching pointers
until both pointers meet in the middle.
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution: 
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        last = slow
        slow = slow.next
        prev = None
        last.next = prev

        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        slow2 = head
        slow = prev
        while slow2 and slow:
            tmp1 = slow2.next
            tmp2 = slow.next
            slow2.next = slow
            slow.next = tmp1
            slow2 = tmp1
            slow = tmp2

