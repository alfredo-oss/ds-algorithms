from LinkedListDesign import ListNode, LinkedList
from typing import List, Optional

"""
I'm given the head of two linked lists list1 and list2.
I have to merge the two lists into one sorted linked list and return the
head of the new sorted linked list.
The new list should be made up of nodes from list1 and list2.
---------------------------
Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
** I could have a list longer than the other**
** I should iterate while both linked lists "exist"**
** If one linked list is empty then the current node should
   point to that list.
** I need a temporary variable that can hold the current values 
   of each list since their pointers are going to be iteratively 
   modified.
"""
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to act as the starting point of the merged list
        dummy = node = ListNode()
        
        # Merge the two lists
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        # Append the remaining elements of list1 or list2
        node.next = list1 or list2 # This line returns either true value
        
        # Return the merged list, which starts at dummy.next
        return dummy.next
