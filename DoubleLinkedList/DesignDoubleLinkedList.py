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
        cur = self.left.next # We initialize our pointer to start at the node that follows the dummy node which would be our actual "head".
        while cur and index > 0: # While the current pointer is not null because we could possibly go out of bounds and the index is greater than 0. This is an alternative technique to modify the position of the pointer, technically you are still iterating over the linked list since the .next and .prev commands are the ones that lead the orientation of the iteration. The counter index serves its own purpose decrementing and allowing 'index' amount of iterations.
            cur = cur.next # On each iteration we will be moving to the right since that is the orientation tha the .next command gives us.
            index -= 1 # We decrement the value of index to allow for iterations.
            if cur and cur != self.right and index == 0: # We check that we didnt go out of bounds, that we are not positioned at the right dummy node and that index has gotten to 0 which is the equivalent of iterating as many times as required.
                return cur.val # If the conditions are met then we return the current value
            return -1 # Else we return -1 indicating we went out of bounds.
    
    def addAtHead(self, val) -> None:
        cur_head = self.left.next
        new_head = ListNode(val)
        self.left.next = new_head
        new_head.next = cur_head
        new_head.prev = self.left
        cur_head.prev = new_head

    def addAtTail(self, val) -> None:
        new_tail = ListNode(val)
        self.tail.next = new_tail
        new_tail.prev = self.tail
        self.tail = new_tail

    def addAtIndex(self, val, index) -> None:
        """
        This method adds the value "val" before the ith index node in the linked list.
        If index equals the length of the linked list, the node will be appended to the end of the linked list thus, we would be calling addAtTail
        If the index is greater than the length, the node will not be inserted.
        """
        curr = self.head
        r = 0
        while r != index and curr:
            curr = curr.next
            r += 1
        if curr and curr.next == None:
            self.addAtTail(val)
        elif curr:
            dummy = curr.prev
            new_node = ListNode(val)
            curr.prev = new_node
            new_node.next = curr
            new_node.prev = dummy
            dummy.next = new_node
    
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        r = 0
        while r != index and curr:
            curr = curr.next
            r += 1
        if curr:
            dummy_right = curr.next
            dummy_left = curr.prev
            dummy_right.prev = dummy_left
            dummy_left.next = dummy_right 