class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i] 
            if diff in map.keys() and i!=map[diff]:
                return [i, map[diff]]
