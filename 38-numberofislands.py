from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0

        max_rows = len(grid)
        max_cols = len(grid[0])

        island_count = 0

        def bfs(r, c):
            q = deque()
            q.append((r,c))

            while q: 
                r,c = q.popleft()
                if r + 1 < max_rows and grid[r + 1][c] == "1": 
                    q.append((r + 1, c))
                if c + 1 < max_cols and grid[r][c + 1] == "1": 
                    q.append((r, c + 1))
                if r > 0 and grid[r - 1][c] == "1": 
                    q.append((r - 1, c))
                if c > 0 and grid[r][c - 1] == "1": 
                    q.append((r, c - 1))
                grid[r][c] = "*"


        for r in range(max_rows):
            for c in range(max_cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    island_count += 1

        return island_count

# from collections import deque

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         max_rows = len(grid)
#         max_cols = len(grid[0])

#         q = deque()
#         islands_count = 0

#         for r in range(max_rows):
#             for c in range(max_cols):
#                 if grid[r][c] == "1":
#                     q.append((r, c))

#         while q: 
#             r, c = q.popleft()
#             if grid[r][c] == "*":
#                 continue
#             island_flag = False
#             if r + 1 < max_rows: 
#                 if grid[r + 1][c] == "*":
#                     island_flag = True
#                 elif grid[r + 1][c] == "1":
#                     q.append((r + 1, c))
#             if r - 1 >=0: 
#                 if grid[r - 1][c] == "*":
#                     island_flag = True 
#                 elif grid[r - 1][c] == "1":
#                     q.append((r - 1, c))
#             if c + 1 < max_cols: 
#                 if grid[r][c + 1] == "*":
#                     island_flag = True
#                 elif grid[r][c + 1] == "1":
#                     q.append((r, c + 1))
#             if c - 1 >= 0: 
#                 if grid[r][c - 1] == "*":
#                     island_flag = True 
#                 elif grid[r][c - 1] == "1":
#                     q.append((r, c - 1))           
        
#             if island_flag != True: 
#                 islands_count += 1
            
#             grid[r][c] = "*"

#         return islands_count