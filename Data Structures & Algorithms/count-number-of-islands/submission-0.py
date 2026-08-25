class Solution:
    def dfs(self, grid: List[List[str]], sr: int, sc: int, n: int, m: int, visited) -> None:
        if sr < 0 or sc < 0 or sr >= n or sc >= m:
            return
        
        
        if grid[sr][sc] == '0':
            visited.add((sr, sc))
            return
        if (sr, sc) in visited: return

        visited.add((sr, sc))
        self.dfs(grid, sr+1, sc, n, m, visited)
        self.dfs(grid, sr-1, sc, n, m, visited)
        self.dfs(grid, sr, sc+1, n, m, visited)
        self.dfs(grid, sr, sc-1, n, m, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        n, m = len(grid), len(grid[0])
        visited = set()

        for i in range(n):
            for j in range(m):
                if len(visited) == n * m:
                    break
                elif (i, j) in visited:
                    continue
                elif grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j, n, m, visited)
                else:
                    visited.add((i,j))
        return count
                    
        