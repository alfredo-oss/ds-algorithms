"""
input: Optional[ListNode] -> representing the head of a Linked List.
output: Optional[ListNode] -> representing the middle of the Linked List.

notes:
------
* The key to this problem is to handle it with two pointers:
    - fast pointer: moves twice as fast through the linked list
    - slow pointer: moves normally through the linked list

* There are two initialization cases:
    - In the case of the linked list having an even amount of 
      nodes, you will have two middle nodes, in which you would
      be asked to return:

        1) The first middle node: 
                                - slow: initialized at head
                                - fast: initialized at head.next

        2) The second middle node:
                                - slow: initialized at the head
                                - fast: initialized at the head

* We are asked to return the complete middle node.

class ListNode:
    def  __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next: # it needs to have a fast.next element otherwise there is no way we can point to fast.next.next
            slow = slow.next
            fast = fast.next.next
        return slow
"""