class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1]>heights[i]:
                index, height = stack.pop()
                res = max(res, ((i - index) * height))
                start = index
            stack.append((start, heights[i]))
        

        while stack:
            res = max(res, (len(heights) - stack[-1][0]) * stack[-1][1])
            stack.pop()
        return res
