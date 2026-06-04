class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        v = "".join(sorted(s))
        w = "".join(sorted(t))
        return v == w