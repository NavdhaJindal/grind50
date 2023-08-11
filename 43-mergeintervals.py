class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) < 2: 
            return intervals

        intervals.sort()

        res = []
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] < intervals[i + 1][0]:
                res.append(intervals[i])
                i += 1
            else: 
                start = intervals[i][0]
                new_end = intervals[i][1]
                while i < len(intervals) - 1 and new_end >= intervals[i + 1][0]: 
                    new_end = max(new_end, intervals[i + 1][1])
                    i += 1
                res.append([start, new_end])
                i += 1

        if intervals[-1][0] > res[-1][1]:
            res.append(intervals[-1])

        return res