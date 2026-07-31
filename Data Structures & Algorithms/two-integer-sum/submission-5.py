class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            candidate = target - nums[i]
            if candidate in hashmap and i != hashmap[candidate]:
                return [i, hashmap[candidate]]