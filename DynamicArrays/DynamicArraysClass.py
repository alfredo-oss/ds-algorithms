class DynamicArray:
    
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity # We need to save the capacity of the array since the definition of dynamic arrays is that they are resizable.
        self.size = 0 # We initialize the size of the array to be 0 since we haven't inserted any values to it
        self.array = [0]*capacity
        

    def get(self, i: int) -> int:
        return self.array[i]
    
    def set(self, i: int, n: int) -> None:
        self.array[i] = n
    
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        
        self.array[self.size] = n
        self.size += 1
    def popback(self, n: int) -> int:
        self.size -= 1
        return self.array[self.size]
    
    def resize(self) -> None:
        self.capacity = self.capacity*2
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
    
    def getSize(self) -> None:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity





arr = DynamicArray(10)
arr.set(4,8)
print(arr.get(4))