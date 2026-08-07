class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        seen = set(nums)

        for i in range(len(nums)):
            if (nums[i]-1) not in seen:
                length = 0
                while (nums[i]+length)in seen:
                    length+=1
                res = max(res, length)
        return res