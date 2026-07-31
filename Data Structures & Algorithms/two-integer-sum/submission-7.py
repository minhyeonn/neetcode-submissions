class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for i, n in enumerate(nums):
            candidate = target - n
            if candidate in map:
                return [map[candidate], i]
            map[n] = i
