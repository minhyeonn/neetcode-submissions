class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = []

        for i, (n1,n2) in enumerate(points):
            dist = n1*n1 + n2*n2
            min_heap.append((dist, n1, n2))

        heapq.heapify(min_heap)

        res = []
        i = 0
        while i<k:
            dist, n1, n2 = heapq.heappop(min_heap)
            res.append([n1, n2])
            i+=1
        return res