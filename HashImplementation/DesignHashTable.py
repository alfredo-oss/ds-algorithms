class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = [None]*self.capacity
    
    def hash_function(self, key):
        return key % self.capacity
    
    def get(self, key) -> int:
        index = self.hash_function(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity

        return -1
    
    
    def insert(self, key, val):
        index = self.hash_function(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.resize()
                return
            elif self.map[index].key == key:
                self.map[index].val = val
                return
            index += 1
            index = index % self.capacity

    def remove(self, key) -> bool:
        index = self.hash_function(key)

        while True:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return True
            index += 1
            index = index % self.capacity
        return False
    
    def resize(self):
        self.capacity = 2 * self.capacity
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.insert(pair.key, pair.val)

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity

        
