class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        cur = newInterval
        for start, end in intervals:
            if cur[1]<start:
                res.append(cur)
                cur = [start, end]
            elif end < cur[0]:
                res.append([start, end])
            else:
                cur = [min(cur[0], start), max(cur[1], end)]
        res.append(cur)

        return res