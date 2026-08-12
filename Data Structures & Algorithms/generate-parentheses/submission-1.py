class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(start, end):
            if start == n and end == n:
                res.append("".join(path))
                return
            if start < n:
                path.append("(")
                backtrack(start + 1, end)
                path.pop()
            if end < start:
                path.append(")")
                backtrack(start, end + 1)
                path.pop()
        backtrack(0, 0)
        return res