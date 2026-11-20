class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = defaultdict(int)
        count_list = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num]+=1
        

        for c in count:
            count_list[count[c]].append(c)
        
        for i in range(len(count_list)-1, -1 ,-1):
            for num in count_list[i]:
                if len(res)==k:
                    break
                res.append(num)
        return res
        

        

        
