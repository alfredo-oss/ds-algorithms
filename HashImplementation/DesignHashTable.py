class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = [None, None]
    
    def hash(self, key) -> int:
        index = 0
        for c in key:
            index += ord(c)
        index = index % self.capacity

    def insert(self, key: int, val: int):
        index = self.hash(key)
        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= (self.capacity//2):
                    self.resize()
                    return
            elif self.map[index].key == key:
                self.map[index].val = val
                return
            index += 1
            index = index % self.capacity

    def get(self, key) -> int:
        index = self.hash(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity

        return None
    
    def remove(self, key: int) -> bool:
        if key not in self.map:
            return False
        index = self.hash(key)
        while True:
            if self.map[index].key == key:
                # This operation could possibly create a hole
                self.map[index] = None
                return True
            index += 1
            index = index % self.capacity
    
    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
    
    def resize(self) -> None:
        newMap = []
        self.capacity = self.capacity*2
        oldMap = self.map
        for i in range(self.capacity):
            newMap.append(None)
        self.map = newMap
        for pair in oldMap:
            if pair:
                self.insert(pair)

        
