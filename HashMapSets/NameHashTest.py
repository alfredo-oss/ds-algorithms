names = ["alice", "brad", "collin", "brad", "dylan", "kim"]
countMap = {}

for name in names:
    if name not in countMap:
        countMap[name] = 1
    else:
        countMap[name] += 1
print(countMap)
helper = []
for element in countMap.keys():
    helper.append(element)
print(countMap.pop(helper[0]))
print(countMap)