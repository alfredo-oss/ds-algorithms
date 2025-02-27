# min heap
class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        # percolate up
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            # perform the swapping
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2
    
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]

        # move last value to root
        self.heap[1] = self.heap.pop()
        i = 1
        # percolate down
        while 2 * i < len(self.heap):
            if (2 * i + 1 < len(self.heap) and 
            self.heap[2 * i + 1] < self.heap[2 * i] and
            self.heap[i] > self.heap[2 * i + 1]):
                # swap right child
                temp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[i] = temp
                # re-assign the index because we moved down the tree since the swapping
                i = 2 * i + 1             
            elif (self.heap[i] > self.heap[2 * i]): # the other conditions are already evaluated on the while and "if" statement
                # swap left child
                temp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = temp

                i = 2 * i
            else:
                break
        return res

    def top(self):
        if len(self.heap) > 1:
            return self.heap[1]
        return None
    
    """
    I'm assuming that heapify consists on giving the structure of a binary heap to a random array
    """

    def heapify(self, arr):
        # 0-th position is moved to the end
        arr.append(arr[0])

        self.heap = arr
        cur = (len(self.heap)-1) // 2

        # the outer loop indicates what node with children are we considering for the "percolate down" operation
        while cur > 0:
            # percolate down
            i = cur
            while 2 * i < len(self.heap): # while the current node has at least a left child 
                if ((2 * i + 1 < len(self.heap)) and
                    (self.heap[2 * i] > self.heap[2 * i + 1]) and 
                    (self.heap[i] > self.heap[2 * i + 1])): # the first thing to check is that we actually have a right child

                    # perform swap with right child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1

                elif (self.heap[i] > self.heap[2 * i]):
                    # perform swap with left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                
                else:
                    break
            cur -= 1
            # since you are modifying the main data structure and
            # that is the function sole's functionality