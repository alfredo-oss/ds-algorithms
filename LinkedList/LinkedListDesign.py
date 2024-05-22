# Single Linked List Node
class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

# Implementation for Singly Linked List
class LinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head