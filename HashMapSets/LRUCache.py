class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
         helper = []
         if len(self.cache) == self.capacity:
            for element in self.cache.keys():
                 helper.append(element)
            self.cache.pop(element[0])     
         self.cache[key] = value