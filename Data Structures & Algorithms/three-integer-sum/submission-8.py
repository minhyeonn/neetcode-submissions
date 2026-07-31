class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1

            while l<r:
                if nums[l] + nums[i] + nums[r] < 0:
                    l+=1
                elif nums[l] + nums[i] + nums[r] > 0: 
                    r-=1
                else:
                    if l>i+1 and nums[l]==nums[l-1]:
                       l+=1
                       continue
                    elif r<len(nums)-1 and nums[r]==nums[r+1]:
                       r-=1
                       continue
                    res.append([nums[l], nums[i], nums[r]])
                    l+=1
        return res
                    
                

