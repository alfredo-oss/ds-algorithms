from typing import List

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
    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while i != index:
            curr = curr.next
        return curr.val
    
    def insertHead(self, val: int) -> None:
        new_head = ListNode(val)
        new_head.next = self.head
        self.head = new_head

    def insertTail(self, val: int) -> None:
        new_tail = ListNode(val)
        self.tail.next = new_tail
        self.tail = new_tail

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while i < index:
            curr = curr.next   
            i += 1

        if curr:
            curr.next = curr.next.next
            return True
        else:
            return False
        
    def getValues(self) -> List[int]:
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr