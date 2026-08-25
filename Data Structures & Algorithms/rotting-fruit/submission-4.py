from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numOnes = 0
        queue = deque([])
        n, m =len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2: queue.append((i,j))
                if grid[i][j] == 1: numOnes += 1
     
        
        time = 0
        while queue:
            print(queue)
            layerSize = len(queue)
            for _ in range(layerSize):
                row, col = queue.popleft()
                dxns = [(0,1), (1,0), (-1,0), (0, -1)]
                for rd, cd in dxns:
                    newRow, newCol = row + rd, col + cd
                    if(
                        min(newRow, newCol) < 0 or 
                        newRow >= n or newCol >= m or
                        grid[newRow][newCol] != 1
                    ) : continue
                    grid[newRow][newCol] = 2
                    numOnes -= 1
                    queue.append((newRow, newCol))
            time += 1
        
        if numOnes: return -1
        if time: return time - 1
        return time
        