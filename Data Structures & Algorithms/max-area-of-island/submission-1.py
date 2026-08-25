class Solution:
    def __init__(self):
        self.count = 0 
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        
        def dfs(row, col):
            if (
                row < 0 or col <0 or
                row >= n or col >= m or
                grid[row][col] == 0 or
                (row, col) in visited
            ) : return 

            self.count += 1
            visited.add((row, col))
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
            return 

        maxCount = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i,j) not in visited:
                    dfs(i,j)
                    if self.count > maxCount:
                        maxCount = self.count
                    self.count = 0
        return maxCount