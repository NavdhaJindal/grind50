class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        new_list = []

        start = newInterval[0]
        end = newInterval[1]

        i = 0

        if not intervals:
            return [newInterval]

        while (i < len(intervals) and intervals[i][1] < newInterval[0]):
            new_list.append(intervals[i])
            i += 1

        while (i < len(intervals) and intervals[i][0] <= newInterval[1]):
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        new_list.append([start, end])

        while (i < len(intervals)):
            new_list.append(intervals[i])
            i += 1

        return new_list
    
        # n = len(intervals)
        # start_index = n
        # end_index = n
        # overlap = False

        # for index in range(len(intervals)):
        #     start = intervals[index][0]
        #     end = intervals[index][1]

        #     if start <= newInterval[0] <= end:
        #         overlap = True
        #         start_index = index

        #     elif start_index == n and start > newInterval[0]:
        #         start_index = index

        #     if start <= newInterval[1] <= end:
        #         overlap = True
        #         end_index = index
            
        #     elif end_index == n and end > newInterval[1]:
        #         end_index = index - 1

        # if end_index == n:
        #     overlap = True
        #     end_index = n-1

        # print('start_index', start_index)
        # print('end_index', end_index)

        # if overlap == False:
        #     intervals.insert(start_index, newInterval)
        #     return intervals