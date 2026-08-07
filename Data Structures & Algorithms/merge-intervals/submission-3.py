class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda i : i[0])
        cur = intervals[0]
        res = []
        for start, end in intervals[1:]:
            if cur[1]<start:
                res.append(cur)
                cur = [start, end]
            else:
                cur = [min(cur[0],start), max(cur[1], end)] 
        res.append(cur)
        return res