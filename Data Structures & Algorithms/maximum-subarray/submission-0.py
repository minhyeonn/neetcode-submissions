class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest_sum = 0
        cur_sum = 0
        for r in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0
                
            cur_sum+=nums[r]

            largest_sum = max(largest_sum, cur_sum)

            if largest_sum==0 and cur_sum < 0:
                largest_sum = min(largest_sum, cur_sum)



        return largest_sum



