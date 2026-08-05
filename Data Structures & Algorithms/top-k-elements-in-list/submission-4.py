class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        final = [[] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        for n, c in count.items():
            final[c].append(n)
        
        res = []

        for i in range(len(final)-1, -1, -1):
            for num in final[i]:
                res.append(num)
                if len(res)==k:
                    return res
