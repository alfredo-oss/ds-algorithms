from typing import List, Optional
from LinkedListDesign import LinkedList, ListNode
"""
The main task here is to invert the pointers of the Linked List and return an inverted list.
## Loop ##
1) I'm on the head node...what do I do?
   - I would like for the next node to point to me.
   - But to keep iterating through the list I need to save the normal logic in a temporary variable or Linked List.
   - If I save the logic in a temporary variable and modify the original one I will me able to restore the logic.
   - I need also a dummy node tail to point the first value to.
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next # I store the cur logic to iterate over the linked list
            curr.next = prev
            prev = curr
            curr = temp
        return prev # Returns prev because that will by default merge the two lists
            