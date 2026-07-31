from collections import deque

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      prefix = []
      for i in range(len(nums)):
        if i==0:
          prefix.append(1)
        else:
          prefix.append(nums[i-1]*prefix[-1])
      suffix = deque()
      for i in range(len(nums)-1,-1,-1):
        if i==len(nums)-1:
          suffix.append(1)
        else:
          suffix.appendleft(nums[i+1]*suffix[0])
      res = []

      for i in range(len(prefix)):
        res.append(prefix[i]*suffix[i])
      return res