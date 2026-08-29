class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res, prevEnd = 0, intervals[0][1]

        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                res += 1
                prevEnd = intervals[i][1]
        
        return res
