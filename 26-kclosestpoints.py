class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        for point in points:
            x, y = point
            dist = sqrt(math.pow(x, 2) + math.pow(y, 2))
            point.append(dist)

        points.sort(key = lambda x: x[2])

        return [[points[i][0], points[i][1]] for i in range(k)]