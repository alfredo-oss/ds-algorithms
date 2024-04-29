from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
    
solution = Solution()
test_1 = "()"
test_2 = "()[]"
test_3 = "(]"

res = solution.isValid(test_1)
print(res)

res = solution.isValid(test_2)
print(res)

res = solution.isValid(test_3)
print(res)