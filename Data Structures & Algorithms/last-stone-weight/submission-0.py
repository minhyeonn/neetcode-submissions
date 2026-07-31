class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap)>1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            diff = -abs(x-y)
            heapq.heappush(max_heap, diff)
        return -max_heap[0] if len(max_heap)==1 else 0
