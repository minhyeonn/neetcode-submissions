from collections import deque

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      res = []
      prefix = []
      suffix = deque()
      
      for i in range(len(nums)):
        if i==0:
          prefix.append(1)
        else:
          prefix.append(prefix[-1]*nums[i-1])
      
       
      for i in range(len(nums)-1, -1, -1):
         if i==len(nums)-1:
          suffix.append(1)
         else:
          suffix.appendleft(suffix[0]*nums[i+1])
        
      for i in range(len(prefix)):
        res.append(prefix[i]*suffix[i])

      return res

