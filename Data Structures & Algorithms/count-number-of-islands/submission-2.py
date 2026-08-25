class Solution:
    def dfs(self, grid: List[List[str]], sr: int, sc: int, n: int, m: int, visited) -> None:

        if (
            sr < 0 or sc < 0 or 
            sr >= n or sc >= m or
            grid[sr][sc] == '0'or 
            (sr, sc) in visited
        ):
            return
        

        visited.add((sr, sc))
        self.dfs(grid, sr+1, sc, n, m, visited)
        self.dfs(grid, sr-1, sc, n, m, visited)
        self.dfs(grid, sr, sc+1, n, m, visited)
        self.dfs(grid, sr, sc-1, n, m, visited)
        return
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        n, m = len(grid), len(grid[0])
        visited = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    self.dfs(grid, i, j, n, m, visited)
        return count
                    
        