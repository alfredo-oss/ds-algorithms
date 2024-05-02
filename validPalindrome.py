class Solution:
    def validPalindrome(self, pal: str) -> bool:

        rev = []
        cpal = []
        
        if pal:
            for i in range(len(pal)-1, -1, -1):
                if  pal[i].lower() not in [",", ".", ";", " ", ":"]:
                    rev.append(pal[i].lower())
            for i in range(len(pal)):
                if  pal[i].lower() not in [",", ".", ";", " ", ":"]:
                    cpal.append(pal[i].lower())
            return rev == cpal
        else:
            print("The string is empty")
            return False

solution = Solution()
test1 = "A man, a plan, a canal: Panama"
test2 = "race a car"
res = solution.validPalindrome(test1)
print(f"Result: {res}")