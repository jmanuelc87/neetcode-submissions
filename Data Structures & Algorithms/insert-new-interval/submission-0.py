class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        result = []

        for i in range(n):
            if intervals[i][0] > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        result.append(newInterval)

        return result