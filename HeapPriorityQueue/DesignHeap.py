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
        
   
