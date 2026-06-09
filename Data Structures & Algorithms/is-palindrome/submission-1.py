class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for i in s.lower():
            if i.isalnum():
                l.append(i)
        return l == list(reversed(l))