class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0: 1}   # empty prefix: sum 0 seen once
        prefix = 0
        res = 0

        for n in nums:
            prefix += n
            res += count.get(prefix - k, 0)
            count[prefix] = count.get(prefix, 0) + 1

        return res
        
