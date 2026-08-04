class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #max heap
        val = [-x for x in stones]
        heapq.heapify(val)

        while len(val) > 1:
            f = heapq.heappop(val)
            s = heapq.heappop(val)
            if f != s:
                heapq.heappush(val, -(s - f))
        
        if len(val) == 1: 
            return abs(val[0]) 
        else:
            return 0