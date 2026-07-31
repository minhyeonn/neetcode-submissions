class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for i in range(len(nums)):
            candidate = target - nums[i]
            if candidate in map:
                return [map[candidate], i]
            map[nums[i]] = i
