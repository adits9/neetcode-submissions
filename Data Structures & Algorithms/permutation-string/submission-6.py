class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s3 = "".join(sorted(s1))
        if len(s1) > len(s2):
            return False
        for i in range(len(s2) + 1 - len(s1)):
            s4 = "".join(sorted(s2[i:i+len(s1)]))
            if s4 == s3:
                return True
        return False