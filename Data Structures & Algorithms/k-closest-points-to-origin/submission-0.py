class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #hashmap + heap
        #run a for loop through points
        minheap = []
        result = []
        heapq.heapify(minheap)

        for i in range(len(points)):
            dist = math.sqrt((points[i][0] - 0) ** 2 + (points[i][1] - 0) ** 2)
            heapq.heappush(minheap, (dist, points[i]))
        for i in range(k):
            result.append(heapq.heappop(minheap)[1])
        return result