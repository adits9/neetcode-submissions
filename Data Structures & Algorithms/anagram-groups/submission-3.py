class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        arr = []
        for n in strs:
            val = "".join(sorted(n))
            arr.append(val)
        for i, n in enumerate(arr):
            if n in m:
                m[f"{n}"].append(strs[i])
            else:
                m[f"{n}"] = [strs[i]]
        return list(m.values())