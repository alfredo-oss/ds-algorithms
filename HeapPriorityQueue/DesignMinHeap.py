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

    def pop(self) -> int:
        
        if len(self.heap) <= 1:
            return None
        # pop the minimum element
        res = self.heap[1]
        # replace the top element with the last element of the array and proceed to percolate it down
        self.heap[1] = self.heap[len(self.heap) - 1]
        i = 1
        while len(self.heap) > 2 * i: # while there is at least a left child

            if (len(self.heap) > 2 * i + 1 and 
                 self.heap[2 * i + 1] < self.heap[2 * i] and
                 self.heap[i] > self.heap[2 * i + 1]):
                # swap with right child
                tmp = self.heap[2 * i + 1]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1

            elif self.heap[2 * i] < self.heap[i]:
                # swap left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return res
    
    def top(self) -> int:
        if len(self.heap) <= 1:
            return None
        return self.heap[1]