# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
#         for point in points:
#             x, y = point
#             dist = sqrt(math.pow(x, 2) + math.pow(y, 2))
#             point.append(dist)

#         points.sort(key = lambda x: x[2])

#         return [[points[i][0], points[i][1]] for i in range(k)]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def calDistance(x: int, y: int):
            return (pow(x, 2) + pow(y, 2))

        heap = []

        for x,y in points: 
            heapq.heappush(heap, (calDistance(x,y), x, y))
        
        k_closest_points = []

        for i in range(k):
            d, x, y = heapq.heappop(heap)
            k_closest_points.append([x, y])

        return k_closest_points