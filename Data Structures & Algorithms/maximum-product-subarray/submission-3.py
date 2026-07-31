class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        res=nums[0]
        max_prod = min_prod = 1

        for i in range(len(nums)):
            if nums[i]==0:
                temp_max = max(nums[i], nums[i] * max_prod, nums[i] * min_prod)
                temp_min = min(nums[i], nums[i] * max_prod, nums[i] * min_prod)
                res = max(res, temp_max)
                min_prod = max_prod = 1
                continue
            temp_max = max(nums[i], nums[i] * max_prod, nums[i] * min_prod)
            temp_min = min(nums[i], nums[i] * max_prod, nums[i] * min_prod)

            max_prod = temp_max
            min_prod = temp_min

            res = max(res, max_prod)
        return res




