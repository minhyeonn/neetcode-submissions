class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            if nums[l]<=nums[r]:
                return nums[l]
            m = (l+r)//2
            ##min is to the right
            if nums[m]>nums[r]:
                l = m+1
            ##min is to the left
            else:
                r = m

