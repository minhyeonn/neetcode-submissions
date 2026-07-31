"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        startArray = sorted([interval.start for interval in intervals])
        endArray = sorted([interval.end for interval in intervals])

        p1 = 0
        p2 = 0
        count = 0
        res = 0
        while p1 < len(startArray):
            if startArray[p1] < endArray[p2]:
                count+=1
                p1+=1
            else:
                count-=1
                p2+=1
            res = max(res,count)
        return res