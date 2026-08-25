from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        queue = deque([(0,0)])
        visited = set((0,0))
        length = 1



        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if (row, col) == (n-1, m-1):
                    return length
                if grid[row][col] == 1:
                    return -1
                dxns = [
                    (0, 1), (1, 0), (0, -1), (-1, 0),
                    (1, -1), (-1, 1), (-1, -1), (1, 1)
                ]

                for rd, cd in dxns:
                    newRow, newCol = row + rd, col + cd
                    if (
                        min(newRow, newCol) < 0 or 
                        newRow >= n or newCol >= m or
                        grid[newRow][newCol] == 1 or
                        (newRow, newCol) in visited
                    ):
                        continue
                    
                    queue.append((newRow, newCol))
                    visited.add((newRow,newCol))
            length += 1
        
        return -1

                        

        