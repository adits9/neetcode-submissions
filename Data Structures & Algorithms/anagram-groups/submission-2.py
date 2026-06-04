class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        arr = []
        final = []
        for n in strs:
            val = "".join(sorted(n))
            arr.append(val)
        for i, n in enumerate(arr):
            if n in m:
                m[f"{n}"].append(strs[i])
            else:
                m[f"{n}"] = [strs[i]]
                final.append(n)
        return list(m.values())