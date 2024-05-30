"""
Simple implementation of a Hash Map where the objective is to assign each unique name to a key
and map that key to a value that represents how many times that name is present in the array.
"""

names = ["alice", "brad", "collin", "brad", "dylan", "kim"]

countMap = {}

for name in names:
    # If countMap does not contain name
    if name not in countMap: # Beautiful property of HashMaps where search is an O(1) operation.
        countMap[name] = 1 # The countMap hashMap is assigned a new key-value pair of the name as a key and the value "1" as an initial count.
    else:
        countMap[name] += 1 # If the name is already mapped into a key-value pair then the count increases by 1.
print(countMap)