class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for n in nums:
            if n in h:
                h[n] += 1
            else:
                h[n] = 1
        data = dict(sorted(h.items(), key=lambda h: h[1], reverse=True))
        l = []
        for v in range(k):
            l.append(list(data)[v])
        return l