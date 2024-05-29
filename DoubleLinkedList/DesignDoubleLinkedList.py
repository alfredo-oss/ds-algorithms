class ListNode:
    def __init__(self, val: int):
        self.prev = None
        self.next = None
        self.val = val

class DoubleLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        
        if self.head.next: # We set curr at self.head.next because Linked Lists are initialized with a dummy node. 
            curr = self.head.next
            r = 0
            while r != index and curr:
                curr = curr.next
                r += 1
            if curr:
                return curr.val
        return -1


