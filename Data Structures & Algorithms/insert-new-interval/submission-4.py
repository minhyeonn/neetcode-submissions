class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        cur_interval = newInterval

        for start, end in intervals:
            if cur_interval[1]<start:
                res.append(cur_interval)
                cur_interval = [start, end]
            elif cur_interval[0]<=end:
                cur_interval = [min(cur_interval[0], start), max(cur_interval[1], end)]
            elif cur_interval[0]>end:
                res.append([start, end])
        res.append(cur_interval)
        

        return res


