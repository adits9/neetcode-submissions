class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for i, n in enumerate(strs):
            s = "".join(sorted(n))
            if s not in h:
                h[s] = [n]
            else:
                h[s].append(n)
        return list(h.values())