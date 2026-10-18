class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        l = list(s)
        pairs_map = {"}":"{", ")":"(", "]":"["}
        for e in l:
            if e in pairs_map and stack and pairs_map[e] == stack[-1]:
                stack.pop()
            else:
                stack.append(e)    
        return len(stack) == 0
