import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minheap = [] 
        def dist(n1, n2):
            return sqrt(n1*n1+n2*n2)
        
        
        n = 0

        for p in points:
            heapq.heappush(minheap, (dist(p[0],p[1]), p[0],p[1]))

        while n<k:
            to_append = heapq.heappop(minheap)
            res.append([to_append[1], to_append[2]])
            n+=1
        return res