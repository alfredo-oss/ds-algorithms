class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None

class DoubleEndedQueue:
    def __init__(self) -> None:
        self.left = self.right = ListNode(0) # We initialize dummy nodes
        self.left.next = self.right
        self.right.prev = self.left

    def append(self, val) -> None:
        node, next, prev = ListNode(val), self.right, self.right.prev
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node


    def appendLeft(self, val) -> None:
        node, next, prev = ListNode(val), self.left.next, self.left
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node
    
    def pop(self) -> int:
        if self.right.prev:
            node, next, prev = self.right.prev, self.right, self.right.prev.prev
            val = node.val
            next.prev = prev
            prev.next = next
            return val
        else:
            return -1

    def popleft(self) -> int:

        if self.left.next:
            node, next, prev =  self.left.next, self.left.next.next, self.left
            val = node.val
            prev.next = next
            next.prev = prev
            return val
        else:
            -1
            

    def isEmpty(self) -> bool:
        return self.left.next == self.right
     
