from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n = len(operations)
        record = []
        for i in range(n):
                if operations[i].lstrip('-').isdigit():
                    record.append(int(operations[i]))

                elif operations[i] == "+":
                    record.append(record[-1] + record[-2])  

                elif operations[i] == "D":
                    record.append(2*record[-1])  

                elif operations[i] == "C":
                    record.pop()
                else:
                    print("Invalid Operation")
        return sum(record)


solution = Solution()
arr = ["5","2","C","D","+"]
res = solution.calPoints(arr)
print(res)
