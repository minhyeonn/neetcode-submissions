class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest_sum = nums[0]
        cur_sum = 0
        for i in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0
            cur_sum+=nums[i]
            largest_sum = max(largest_sum, cur_sum)
            
        return largest_sum



