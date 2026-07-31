class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []
        
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        for val in count:
            freq[count[val]].append(val)
        
        for i in range(len(freq)-1, -1,-1):
            if freq[i]:
                for num in freq[i]:
                    if len(res)==k:
                        return res
                    else:
                        res.append(num)
        return res 
            

        
        

        



        

            

        
