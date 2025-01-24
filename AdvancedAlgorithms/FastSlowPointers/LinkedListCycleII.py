"""
input: Optional[ListNode]
output: Optional[ListNode]

Given the head of a Linked List, return the node where the cycle begins. If there is no cycle return null.
notes:
------
* we already know how to find if there is a cycle. 
    - If this is the case our pointers will be set at the point of intersection.
    - If that is not the case and either fast = null or fast.next is = null, we found that there is no cycle.
* we also know that the distance between a second slow pointer starting at the head and the original slow pointer
  starting at the intersection will be equal in order to get to the starting point of the cycle.
"""
from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast == None or fast.next == None:
            return None
        slow2 = head
        while slow2 != slow:
            slow = slow.next
            slow2 = slow2.next
        return slow2