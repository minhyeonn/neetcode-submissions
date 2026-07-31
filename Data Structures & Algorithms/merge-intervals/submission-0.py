class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        
        res = []
        cur_interval = intervals[0]

        for i in range(1, len(intervals)):
            
            if intervals[i][0] > cur_interval[1]:
                res.append(cur_interval)
                cur_interval = intervals[i]
            else:
                cur_interval = [min(cur_interval[0], intervals[i][0]), max(cur_interval[1], intervals[i][1])]
                
        res.append(cur_interval)
        return res