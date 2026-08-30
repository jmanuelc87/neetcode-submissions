"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x:x.start)
        n = len(intervals)
        prevEnd = intervals[0]

        for i in range(1, n):
            if prevEnd.end > intervals[i].start:
                return False
            else:
                prevEnd = intervals[i]
        
        return True