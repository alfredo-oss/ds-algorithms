from typing import List
# Definition of a pair

pairs = [(3, "cat"), (3, "bird"), (2, "dog")]

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

def InsertionSort(pair: List[Pair]) -> List[Pair]:
    iter = []
    for i in range(len(pairs)):
        j = 0
        while j >=0 and pairs[j+1][0] < pairs[j][0]:
            temp = pairs[j+1] 
            pairs[j+1] = pairs[j]
            pairs[j] = temp
            j-=1
            iter.append(pairs)
            
    return iter

print(InsertionSort(pairs))