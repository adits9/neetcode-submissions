class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        srev = "".join(sorted(s))
        trev = "".join(sorted(t))
        if srev == trev:
            return True
        return False