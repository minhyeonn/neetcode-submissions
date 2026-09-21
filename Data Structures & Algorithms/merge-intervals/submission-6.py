class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        cur_interval = intervals[0]
        
        res = []
        for i in range(1, len(intervals)):
            if cur_interval[1]>=intervals[i][0]:
                cur_interval = [min(cur_interval[0], intervals[i][0]), max(cur_interval[1], intervals[i][1])]
            elif cur_interval[1]<intervals[i][0]:
                res.append(cur_interval)
                cur_interval = intervals[i]
            
        res.append(cur_interval)
        return res