class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sub = []
        mlength = 0

        for r in range(len(s)):
            while s[r] in sub:
                length = len(sub)
                mlength = max(length, mlength)
                sub.pop(0)
            sub.append(s[r])

        mlength = max(mlength, len(sub))
        return mlength