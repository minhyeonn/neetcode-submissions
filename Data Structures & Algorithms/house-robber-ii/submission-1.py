class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def HouseRobberOne(range1, range2):
            rob1, rob2 = 0, 0
            for i in range(range1, range2):
                tmp = max(rob2, rob1 + nums[i])
                rob1 = rob2
                rob2 = tmp
            return rob2

        return max(HouseRobberOne(0,len(nums)-1), HouseRobberOne(1, len(nums)))