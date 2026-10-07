class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        res = []
        for i in range(len(nums)):
            count[nums[i]]+=1
        
        for num in count:
            if count[num]>len(nums)//3:
                res.append(num)
        return res