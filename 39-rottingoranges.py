class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = collections.deque()
        fresh_set = set()

        if not grid: 
            return 0

        max_rows = len(grid)
        max_cols = len(grid[0])

        def makeRotten(r,c):
            if r + 1 < max_rows and (r + 1, c) in fresh_set:
                fresh_set.remove((r + 1, c))
                grid[r + 1][c] = 2
                q.append((r + 1, c))
            if r - 1 >=0 and (r - 1, c) in fresh_set:
                fresh_set.remove((r - 1, c))
                grid[r - 1][c] = 2
                q.append((r - 1, c))
            if c + 1 < max_cols and (r, c + 1) in fresh_set:
                fresh_set.remove((r, c + 1))
                grid[r][c + 1] = 2
                q.append((r, c + 1))
            if c - 1 >=0 and (r, c - 1) in fresh_set: 
                fresh_set.remove((r, c - 1))
                grid[r][c - 1] = 2
                q.append((r, c - 1))

        for r in range(max_rows): 
            for c in range(max_cols): 
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh_set.add((r,c))

        minutes = 0
        counter = len(q)

        while fresh_set and counter > 0: 
            r, c = q.popleft()
            grid[r][c] = 0
            counter -= 1
            makeRotten(r,c)
            if counter == 0 or not fresh_set:
                minutes += 1
                counter = len(q)

        return minutes if not fresh_set else -1