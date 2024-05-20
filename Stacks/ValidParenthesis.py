"""
I'm given a string consisting of all the possible "parentheses", in different order and I need to check if the string is valid or not.
A string is valid when:
1. Every open bracket is closed by the same type of close bracket.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
The function should return true or false depending on the state of the string.

Example:
---------------------
Input: s = "([{}])"

Output: true
---------------------
Input: s = "[(])"

Output: false
---------------------

Fred Solution:
---------
1. First I need to create a map of what is the closing bracket of each one of the posibilities.
2. Next I need to be able to iterate inside the string up until the point of finding a closing bracket.
3. When finding a closing bracket, I need to check if the previous value from that closing bracket is actually the matching pair in the map.
4. !! You can't pop from the middle. Popping is at the end so you actually have to split the array pretty much and then check if the splitted array contains the matching bracket.
5. Else dont do anything.
6. Return true if the array is empty.
7. Return false if the array contains elements.

NeetCode Solution:
------------------
It was actually not necessary to work with the stack "In Place". It was way easier to create an auxiliari array. Lets see how it goes.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        string_map = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        stack = []

        for string in s:
            if string not in string_map: # This checks for any opening brackets
                stack.append(string)
                continue
            if not stack or stack[-1] != string_map[string]: # This might be checking if the stack comes empty.
                return False
            stack.pop()
        return not stack # If stack has elements it will be true, but the negation statement returns the inverse.
    
solution = Solution()
test_1 = "([{}])"
test_2 = "[(])"
print(solution.isValid(test_2))