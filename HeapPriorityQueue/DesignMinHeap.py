class MinHeap:
    """
    class MinHeap helps us structure our arrays in a way that it is easier to retrieve minimum elements.
    
    ----
    A conventional way to traverse these datastructures is:
    left child: 2 * i
    right child: 2 * i + 1
    parent: 
    """

    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:

        self.heap.append(val)
        # once we insert the value into the queue we need to start traversing and formatting the tree so it meets the structure and order properties
        i = len(self.heap) - 1
        
        # it doesnt matter where we insert the value, the process once its in the Heap its to percolate it up
        # in the percolate up algorithm the comparison (between the child and parent node) is done in the while statement
        while i > 1  and self.heap[i] < self.heap[i // 2]:
            # if the conditions are met we have to swap the values
            tmp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = tmp
            i = i//2
