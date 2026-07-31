class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        rob1=nums[0]
        rob2=max(rob1, nums[1])


        for i in range(2,len(nums)):
            tmp = max(rob2, rob1+nums[i])
            rob1 = rob2
            rob2 = tmp
        return rob2


