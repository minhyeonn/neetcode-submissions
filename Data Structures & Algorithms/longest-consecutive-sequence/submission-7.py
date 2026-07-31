class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ordered_nums = sorted(nums)


        count = [1] * len(ordered_nums)

        i = 1
        j=0
        while i < len(ordered_nums):
            if ordered_nums[i-1]+1 == ordered_nums[i]:
                count[j] += 1
                i += 1
            elif ordered_nums[i-1] == ordered_nums[i]:
                i += 1
            else: 
                j+=1
                i += 1
        res = 0
        for num in count:
            if(num>res):
                res = num
        
        return res
            
            






