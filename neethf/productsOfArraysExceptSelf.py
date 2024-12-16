"""
input: List[int]
output: List[int] 
We receive an integer array and we need to return the multiplications of all the elements but,
the specific index.

example:
--------
nums = [1,2,4,6]
result = [48,24,12,8]

the challenging part here is to be able to go back to the beggining, without taking into account the current element.
so, for example i could do:

Brute Force:
------------
res_arr = []
visit = set()
for idx, _ in enumerate(nums):
    visit.add(idx)
    res = 1
    for idx_sub, element in enumerate(nums):
        if idx_sub not in visit:
            res *= element
    res_arr.append(res)
    visit.remove(idx)
return res_arr

"""