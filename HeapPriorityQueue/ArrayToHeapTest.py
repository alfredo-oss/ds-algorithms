from MinHeap import Heap

heapcls = Heap()
arr = [60, 50, 80, 40, 30, 10, 70, 20, 90]

resheap = heapcls.heapify(arr)

# to access a constructor variable you need to call the property of the instantiation
print(heapcls.heap)