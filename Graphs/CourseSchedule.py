"""
* You are given an input: [array of prerequisites]
  where prerequisites[i] = [a_i, b_i]

  lets assume courses need to be taken in order.
* [[a_0, b_0], [a_1, b_1], [a_2, b_2]]

* there are also a total of numCourses you are required to take, 
  labeled from 0 to numCourses-1 (it might be 0 indexed)

* return true just in case we are able to take a number of courses

solution:
--------
* we have a directed graph, because a course needs to be taken to take the current course
* for each element we have a source and a destination.
    -> if a source has a destination, there cant be an addition of 
       the inversion of that. in that case there has to be a False return.
* now, we also have the numCourses which would set our return value to be true:
    -> How do we account for it?
    -> can we add the source and destination?
"""
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to a prereq list
        preMap = {i:[] for i in range(numCourses)} # there are a ton of ways to go about this but, here we are declaring in a "Pythonic" way, the preMap structure with all of the courses as key: i to a list of neighbors.
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet = all courses along the curr DFS path
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for prereq in preMap[crs]:
                if not dfs(prereq): return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        # this final loop handles the case where we have courses and pre-requisites that are not connected
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True