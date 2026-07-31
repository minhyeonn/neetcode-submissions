class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = 0
        for l in range(len(nums)):
            cur_res = 1
            for r in range(l, len(nums)):
                cur_res *= nums[r]
                res = max(res, cur_res)
        return res
            
