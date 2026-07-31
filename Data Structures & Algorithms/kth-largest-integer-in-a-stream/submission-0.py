class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = [-n for n in nums]
        heapq.heapify(self.max_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, -val)
        temp = self.max_heap.copy()
        for i in range(self.k):
            res = heapq.heappop(temp)
        return -res
