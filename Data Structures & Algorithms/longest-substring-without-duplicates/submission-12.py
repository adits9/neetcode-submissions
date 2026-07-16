class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = []
        maxlen = 0
        for i in s:
            if i not in q:
                q.append(i)
            else:
                maxlen = max(len(q), maxlen)
                while i in q:
                    q.pop(0)
                q.append(i)
        maxlen = max(len(q), maxlen)
        return maxlen