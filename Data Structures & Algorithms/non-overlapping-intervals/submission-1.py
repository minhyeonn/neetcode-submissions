class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        new_interval_array = [intervals[0]]
        cur_interval = intervals[0]

        for i in range(1, len(intervals)):
            
            if intervals[i][0] >= cur_interval[1]:
                cur_interval = intervals[i]
                new_interval_array.append(cur_interval)
            else:
                if intervals[i][1] < cur_interval[1]:
                    cur_interval = intervals[i]
                    new_interval_array[-1] = cur_interval

        return len(intervals) - len(new_interval_array)


        