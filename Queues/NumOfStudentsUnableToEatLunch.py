from typing import List
"""
This problem is beautifully resolved with a HashMap
"""
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = {} # We initialize the hashmap
        for s in students:
            if s not in cnt:
                cnt[s] = 0
            cnt[s]+=1
        
        for s in sandwiches: # This serves a sandwich in order so if you have a sandwich that does not match any customers, then thats the amount of customers you will have left to serve.
            if cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                return res
        
        return res
            

