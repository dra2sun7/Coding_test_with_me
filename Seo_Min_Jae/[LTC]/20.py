class Solution:
    def isValid(self, s: str) -> bool:
        dict = {')': '(', '}': '{', ']':'['}
        stack = []
        
        for p in s:
            if p not in dict:   # 여는 괄호
                stack.append(p)
            elif not stack or dict[p] != stack[-1]:   # stack이 없거나 닫는 괄호와 짝이 안 맞는 경우
                return False
            else:
                stack.pop()
        
        if stack:
            return False
        
        return True

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {"(":")", "{":"}", "[":"]"}

        for w in s:
            if w in par:
                stack.append(w)
            else:
                if stack and par[stack[-1]] == w:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False

        return True