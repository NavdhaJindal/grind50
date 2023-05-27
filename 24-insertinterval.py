class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        start_index = n
        end_index = n
        overlap = False

        for index in range(len(intervals)):
            start = intervals[index][0]
            end = intervals[index][1]

            if start <= newInterval[0] <= end:
                overlap = True
                start_index = index

            elif start_index == n and start > newInterval[0]:
                start_index = index

            if start <= newInterval[1] <= end:
                overlap = True
                end_index = index
            
            elif end_index == n and end > newInterval[1]:
                end_index = index - 1

        if end_index == n:
            overlap = True
            end_index = n-1

        print('start_index', start_index)
        print('end_index', end_index)

        if overlap == False:
            intervals.insert(start_index, newInterval)
            return intervals