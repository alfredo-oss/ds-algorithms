class Pair:
    def __init__(self, key: int, val) -> None:
        self.key = key
        self.val = val

class HashMap:
    def __init__(self, capacity: int) -> None:
        self.size = 0
        self.capacity = 2 # Defining a default value for capacity
        self.map = [None, None] # Initializing the empty array that will hold the HashMap under the hood
    
    def hash(self, key: int) -> int:
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity
    
    def get(self, key):
        index = self.hash(key) # by hashing the searched key we "should" immediately get to the value
        # since we established the open addressing policy we immediately look for the key which should be at the spot or immediately after
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity # we keep the index inbounds
        return None
    
    def put(self, key, val):
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= (self.capacity//2):
                    self.rehash() 
                    return
            elif self.map[index].key == key:
                self.map[index].val = val
                return
            index += 1
            index = index % self.capacity

    def remove(self, key): # this remove function does not solve the bug for creating holes
        if not self.get(key):
            return
        
        index = self.hash(key)
        while True:
            if self.map[index] == key:
                # Removing an element using open-addressing actually causes a bug,
                # because may create a hole in the list and our get() method would
                # stop searching early because of this bug
                self.map = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity

    def rehash(self):
        self.capacity = 2 * self.capacity
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)
        
        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)

    def print(self):
        for pair in self.map:
            if pair:
                print(pair.key, pair.val)


