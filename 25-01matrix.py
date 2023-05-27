from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        queue = deque()
        new_mat = mat
        m = len(mat)
        n = len(mat[0])

        if not (mat and mat[0]): 
            return mat

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    new_mat[r][c] = 0
                    queue.append((r, c))
                
                else:
                    new_mat[r][c] = -1 

        while queue: 
            r, c = queue.popleft()
            distance = new_mat[r][c] + 1
            if (r - 1) >= 0:
                if new_mat[r-1][c] == -1:
                    new_mat[r-1][c] = distance
                    queue.append((r-1, c))
            if (c + 1) < n:
                if new_mat[r][c+1] == -1:
                    new_mat[r][c+1] = distance
                    queue.append((r, c+1))
            if (c - 1) >= 0:
                if new_mat[r][c - 1] == -1:
                    new_mat[r][c - 1] = distance
                    queue.append((r, c-1))
            if (r + 1) < m:
                if new_mat[r+1][c] == -1:
                    new_mat[r+1][c] = distance
                    queue.append((r+1, c))
        
        return new_mat