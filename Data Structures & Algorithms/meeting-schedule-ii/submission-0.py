"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_arr = [ j.start for j in intervals]
        end_arr = [ j.end for j in intervals]

        start_arr.sort()
        end_arr.sort()

        s, e, count, res = 0, 0, 0, 0

        while s < len(intervals):
            if start_arr[s] < end_arr[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        
        return res