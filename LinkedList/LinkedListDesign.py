from typing import List

# Single Linked List Node
class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

# Implementation for Singly Linked List
class LinkedList:

    def __init__(self):
        # Dummy node
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next # This is set to self.head.next because we know that there is always an initialization of 
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1 # Index out of bounds
    
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next # We are setting this because we have the dummy node and we don't want the new head pointing to the dummy node
        self.head.next = new_node
        if not new_node.next:
            # If list was empty before inserting
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head # This is an important point. To do operations with Linked List Nodes we need to operate with the node that is in the position before the node of interest. So, we don't start from self.head.next we start from self.head.
        while i < index and curr:  
            # Move curr to node before target node
            i += 1
            curr = curr.next 
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        else:
            return False
        
    def getValues(self) -> List[int]:
        arr = []
        curr = self.head.next # Because we don't want to include the value of the dummy node
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr