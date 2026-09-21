class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0

        seen = set(nums)

        for i in range(len(nums)):
            if nums[i]-1 not in seen:
                cur = nums[i]
                while cur+1 in seen:
                    cur+=1
                res = max(res, cur - nums[i] + 1)
        return res