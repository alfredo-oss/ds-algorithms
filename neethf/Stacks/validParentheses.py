"""
input: list[str] # list of parentheses
output: bool # response indicating if the parenthesis is valid or not

notes:
-----
* we are given all the types of possible characters that can form our string
  so, it makes sense to use a hashmap to store the corresponding closing parenthesis
  as a value.

* our hashmap would look like this:
    {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }
* the key conditions are that, in order of appearance,
  the closing parenthesis needs to be after the opening parenthesis,
  which could translate in us checking for the inclusion of each 
  element analyzed from the array.
    -> which we could achieve from either poping the element
       from left or right.
* this previous thought brings me to what might be the solution.
    pseudocode:
    ----------
    while the string has elements:
        leftElement = string.popleft()
        rightElement = string.popright()
        if hashmap[leftElement] != rightElement:
            return False
    return True # we return True once the list has no elements
* there is a way of transforming a string to a list of each element
  which presumably requires O(n) complexity and I can't remember right now
  so, I will proceed through iterating over the elements of the string and 
  appending them to an auxiliary array. This is because arrays in Python have 
  the .pop() and .popleft() methods that we require for this approach.
"""
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        aux = [element for element in s]
        aux = deque(aux)
        while aux:
            leftElement = aux.popleft()
            rightElement = aux.pop()
            if parMap[leftElement] != rightElement:
                return False
        return True