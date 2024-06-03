class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None

class DoubleLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
    
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
