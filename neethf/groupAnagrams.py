"""
input: strings: List[str]
output: List[List[str]]
-- notes --
* strs that cant be rearranged to another string should be returned
  on a list by itself.
* strs that can should be grouped together.
* edge cases:
  some strings can be of different length

solution(single pair):
--------
# helper function
s = "eat"
t = "tea"
countS = {}
countT = {}
if len(str1) != len(str2):
    keep going (set to boolean)
for i in range(len(str1)):
    countS[s[i]] = 1 + count1.get(s[i], 0)
    countS[t[i]] = 1 + count1.get(t[i], 0)
return countS == countT

solution(entire array):
----------------------
res = []
for i in range(len(strings)):
    aux = []
    aux.append(strings[i])
    for j in range(i, len(strings)):
        if helper(strings[i], strings[j]):
            aux.append(strings[j])
    res.append(aux)
return res
    
"""
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()