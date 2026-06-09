class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vals = []
        for s in strs:
            vals.append("".join(sorted(s)))
        h = {}
        for i, v in enumerate(vals):
            if v in h:
                h[v].append(strs[i])
            else:
                h[v] = [strs[i]]
        return list(h.values())