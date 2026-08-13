class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        cur = intervals[0]

        for start, end in intervals[1:]:
            if cur[1]<=start:
                cur = [start, end]
            else:
                res+=1
                cur = [min(cur[0], start), min(cur[1], end)]
        return res

            



