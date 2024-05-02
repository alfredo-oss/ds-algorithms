from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s: # For each character in the given string.
            print(f"{c}")
            if c in closeToOpen: # If the character is a key in the HashMap.
                if stack and stack[-1] == closeToOpen[c]: # Then we check if the stack is empty or not, if its not we concurrently check if the previous value from the stack (referencing the top one) matches the closing value assigned on the HashMap.
                    print(f"{stack},{closeToOpen[c]}")
                    stack.pop() # If it matches then we remove the value since it's not a concern anymore. 
                    print(f"{stack}")
                else: # Then, "else" handles any other cases like, having elements inside the stack, but not having a matching opening parentheses referencing the HashMap.
                    return False
            else: # If a key does not match the closing characteristics it will be added to the stack
                print(stack)
                stack.append(c)
                print(stack)
        return True if not stack else False # Then we return True if the stack is empty and false if the stack is not since we couldnt find an opening parentheses while referencing the HashMap.
    
solution = Solution()
test_1 = "[()]{}"

res = solution.isValid(test_1)
print(res)
