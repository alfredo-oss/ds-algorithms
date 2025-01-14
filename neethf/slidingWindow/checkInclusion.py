"""
input: s1: str, s2: str
output: bool

notes:
-----
* we are asked to solve this problem in O(n) time and O(1) space.

* the problem statement gives us a hint of the strings only containing a - z letters

* one way to account for this is to have 2, 26 elements in two different hashmaps accounting for the amount of letters.
    -> and this is one thing to take into account, since you are operating with only 26 letters, and that
       will be THE size of the array for the WHOLE time. Thus, this makes the case for O(1) space.

* these two hashmaps will be backing up our sliding window approach.

* we also need to initialize our matches variable in order to not have to compare all the elements in the hashmaps

solution:
--------
s1Count = {}
s2Count = {}
matches = 0

for _ in s1:

"""