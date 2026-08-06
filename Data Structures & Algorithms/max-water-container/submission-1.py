class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res = (r-l)*min(heights[l], heights[r])
        while l<r:
            if heights[l]<heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            else:
                l+=1
                r-=1
            res = max(res, (r-l)*min(heights[l], heights[r]))
        return res