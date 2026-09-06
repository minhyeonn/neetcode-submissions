class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for i in range(len(nums)):
            heapq.heappush(max_heap, -nums[i])

        while k!=0:
            res = -heapq.heappop(max_heap)
            k-=1
        return res

        