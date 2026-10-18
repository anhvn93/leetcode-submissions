class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        l = list(s)
        if len(l)==1:
            return False
        for e in l:
            print(e)
            if stack:
                if e ==")" and stack[-1] == "(" :
                    stack.pop()
                elif e =="}" and stack[-1] == "{" :
                    stack.pop()
                elif e =="]" and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(e)
            else:
                stack.append(e)
            print(stack)
        print(stack)
        return len(stack) == 0
