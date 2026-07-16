class Solution:
    def isValid(self, s: str) -> bool:
        h = {')':'(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            if i in h:
                if stack and stack[-1] == h[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True