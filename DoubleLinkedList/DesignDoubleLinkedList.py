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
        """
        We start by assigning the main nodes we will be operating with to shorter named variables,
        so it becomes easier to handle them along the code.
        Since we know we are operating at the head of the linked list and we will have to be 
        linking the new node to one previously and another one following the node we want to 
        insert. 
        ** The previous node: Left dummy node [We always want to keep this node alive].
        ** The actual node: Declaration of a node with the value we want to insert.
        ** The following node: The inmediate node that follows the next dummy node.
        """
        node, next, prev = ListNode(val), self.left.next, self.left
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def addAtTail(self, val) -> None:
        node, next, prev = ListNode(val), self.right, self.right.prev
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def addAtIndex(self, val, index) -> None:
        """
        This method adds the value "val" before the ith index node in the linked list.
        If index equals the length of the linked list, the node will be appended to the
        end of the linked list thus, we would be calling addAtTail.
        If the index is greater than the length, the node will not be inserted.
        """
        cur = self.left.next # We initialize our pointer to start at the node that follows the dummy node which would be our actual "head".
        while cur and index > 0: # While the current pointer is not null because we could possibly go out of bounds and the index is greater than 0. This is an alternative technique to modify the position of the pointer, technically you are still iterating over the linked list since the .next and .prev commands are the ones that lead the orientation of the iteration. The counter index serves its own purpose decrementing and allowing 'index' amount of iterations.
            cur = cur.next # On each iteration we will be moving to the right since that is the orientation tha the .next command gives us.
            index -= 1 # We decrement the value of index to allow for iterations.
            
        if cur and index == 0: # We check that we didnt go out of bounds, that we are not positioned at the right dummy node and that index has gotten to 0 which is the equivalent of iterating as many times as required.
            node, next, prev = ListNode(val), cur, cur.prev
            prev.next = node
            node.prev = prev
            node.next = next
            next.prev = node
            
    
    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index == 0:
            prev, next = cur.prev, cur.next
            prev.next = next
            next.prev = prev


def test_double_linked_list():
    # Initialize the double linked list
    dll = DoubleLinkedList()

    # Add elements at head
    dll.addAtHead(1)
    dll.addAtHead(2)
    dll.addAtHead(3)
    
    # Add elements at tail
    dll.addAtTail(4)
    dll.addAtTail(5)
    
    # Add element at index 2 (0-based index)
    dll.addAtIndex(6, 2)
    
    # Get elements and check if they are correct
    assert dll.get(0) == 3, f"Expected 3, got {dll.get(0)}"
    assert dll.get(1) == 2, f"Expected 2, got {dll.get(1)}"
    assert dll.get(2) == 6, f"Expected 6, got {dll.get(2)}"
    assert dll.get(3) == 1, f"Expected 1, got {dll.get(3)}"
    assert dll.get(4) == 4, f"Expected 4, got {dll.get(4)}"
    assert dll.get(5) == 5, f"Expected 5, got {dll.get(5)}"
    
    # Delete element at index 2
    dll.deleteAtIndex(2)
    
    # Check the list after deletion
    assert dll.get(0) == 3, f"Expected 3, got {dll.get(0)}"
    assert dll.get(1) == 2, f"Expected 2, got {dll.get(1)}"
    assert dll.get(2) == 1, f"Expected 1, got {dll.get(2)}"
    assert dll.get(3) == 4, f"Expected 4, got {dll.get(3)}"
    assert dll.get(4) == 5, f"Expected 5, got {dll.get(4)}"

    print("All test cases passed!")

# Run the test
test_double_linked_list()
