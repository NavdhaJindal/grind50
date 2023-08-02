from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_rows = len(grid)
        max_cols = len(grid[0])

        q = deque()
        islands_count = 0

        for r in range(max_rows):
            for c in range(max_cols):
                if grid[r][c] == "1":
                    q.append((r, c))

        while q: 
            r, c = q.popleft()
            if grid[r][c] == "*":
                continue
            island_flag = False
            if r + 1 < max_rows: 
                if grid[r + 1][c] == "*":
                    island_flag = True
                elif grid[r + 1][c] == "1":
                    q.append((r + 1, c))
            if r - 1 >=0: 
                if grid[r - 1][c] == "*":
                    island_flag = True 
                elif grid[r - 1][c] == "1":
                    q.append((r - 1, c))
            if c + 1 < max_cols: 
                if grid[r][c + 1] == "*":
                    island_flag = True
                elif grid[r][c + 1] == "1":
                    q.append((r, c + 1))
            if c - 1 >= 0: 
                if grid[r][c - 1] == "*":
                    island_flag = True 
                elif grid[r][c - 1] == "1":
                    q.append((r, c - 1))           
        
            if island_flag != True: 
                islands_count += 1
            
            grid[r][c] = "*"

        return islands_count