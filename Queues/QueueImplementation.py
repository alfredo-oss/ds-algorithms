"""
This is a class implementation for a Queue, on top of a Single Linked List.
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = next
    
class Queue:
    # Implementing this with dummy nodes would be easier!
    def __init__(self):
        self.left = self.right = None # Head and tail are initialized as "None" when the queue is empty 
    
    def enqueue(self, val):
        newNode = ListNode(val)

        # Queue is non-empty
        """
        When the queue is not empty only the 'right' or 'tail' pointer is updated. This is 
        because we need to keep the 'head' or 'left' pointer static until a dequeue process
        is requested. 
        """
        if self.right:
            self.right.next = newNode
            self.right = self.right.next
        # Queue is empty
        else:
            self.left = self.right = newNode
    
    def dequeue(self):
        # Queue is empty
        self.isEmpty()
        
        # Remove left node and return value
        val = self.left.val
        self.left = self.left.next
        if not self.left: # If by de-linking that head or left pointer, we ran out of elements in the queue.
            self.right = None # We set the right pointer to be None, going back to the initial values that the constructor sets.
        return val
    
    def isEmpty(self):
        # Queue is empty
        if not self.left:
            return None
    
    def print(self):
        cur = self.left
        while cur:
            print(cur.val, ' -> ', end="")
            cur = cur.next
        print()



        
    
