class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest_sum = nums[0]
        cur_sum = 0
        for r in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0
            cur_sum+=nums[r]
            largest_sum = max(largest_sum, cur_sum)
            



        return largest_sum



