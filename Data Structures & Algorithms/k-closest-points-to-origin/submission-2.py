class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []
        min_heap = []

        for x, y in points:
            dist = (x*x+y*y)**0.5
            heapq.heappush(min_heap, [dist, x, y])

        while k>0:
            res.append([min_heap[0][1], min_heap[0][2]])
            heapq.heappop(min_heap)
            k-=1
        return res
