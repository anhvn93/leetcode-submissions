class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        total = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                ans.append(ans[-1] + ans[-2])
                total += ans[-1]
            elif operations[i] == "D":
                ans.append(ans[-1] *2)
                total += ans[-1]
            elif operations[i] == "C":
                e = ans.pop(-1)
                total -= e
            else: 
                ans.append(int(operations[i]))
                total += ans[-1]
        return total