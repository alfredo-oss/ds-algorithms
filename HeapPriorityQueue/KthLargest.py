from MinHeap import *

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.heapmin = Heap()
        self.k = k
        self.minHeap = nums
        self.heapmin.heapify(self.minHeap)
        while len(self.minHeap) > k:
            self.heapmin.pop(self.minHeap)

    def add(self, val: int) -> int:
        self.heapmin.push(self.minHeap, val)
        if len(self.minHeap) > self.k:
            self.heapmin.pop(self.minHeap) # we want to pop the "excess" of data
        return self.minHeap[0]


