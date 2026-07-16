class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in {"+", "-", "/", "*"}:
                stack.append(int(t))
            else:
                right = int(stack.pop())
                left = int(stack.pop())

                if t == "+":
                    stack.append(right + left)
                elif t == "-":
                    stack.append(left - right)
                elif t == "*":
                    stack.append(right * left)
                elif t == "/":
                    stack.append(left / right)
        return int(stack[0])