class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda i: i[0])
        
        cur_interval = intervals[0]

        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0]<=cur_interval[1]:
                cur_interval = [min(intervals[i][0], cur_interval[0]), max(intervals[i][1], cur_interval[1])]
            else:
                res.append(cur_interval)
                cur_interval = intervals[i]
        res.append(cur_interval)

        return res