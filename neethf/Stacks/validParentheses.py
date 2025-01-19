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
        ")" : "(",
        "}" : "{",
        "]" : "["
    }
* the key conditions are that, in order of appearance,
  the closing parenthesis needs to be after the opening parenthesis,
  which could translate in us checking for the inclusion of each 
  element analyzed from the array.
* the catch here is the way in which we check for inclusion. basically, what 
  we need to do is iterate through every element:
    -> what we will do on each iteration is to ask:
        -> is the element in our hashmap?
            -> if it is then check if the last element
               of the stack is exactly the corresponding
               value of the hashmap.[why?] - because that's the order 
               of closings that we defined.
               -> if this is not met then we need to return False
        -> if the element is not on the hashmap which means that we 
           which means that we are facing an opening character, then
           we need to add that element to our stack.
* remember that we can use a list to represent a stack:
    [left most element] : arr[0] (just as reference)
    [right most element] : arr[-1] (in the case of arrays we can easily
    remove the right most element, which is the last appended element to 
    the stack with the .pop() method) 
"""

class Solution:
    def isValid(self, s: str) -> bool:
        refMap = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []
        for c in s:
            if c in refMap:
                if stack and refMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False