class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        cur_interval = intervals[0]
        for i in range(1, len(intervals)):
            if cur_interval[1]<=intervals[i][0]:
                cur_interval = intervals[i]
            else:
                cur_interval = [cur_interval[0], min(cur_interval[1],intervals[i][1])]
                res+=1
        return res
        
            



