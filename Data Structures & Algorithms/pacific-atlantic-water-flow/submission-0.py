class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(row, col, visited, prevHeight):
            if min(row, col) < 0 or row >= ROW or col >= COL or (row, col) in visited or heights[row][col] < prevHeight:
                return
            
            visited.add((row, col))
            dxns = [(0,1), (1,0), (0, -1), (-1, 0)]
            for x,y in dxns:
                dfs(row+x, col+y, visited, heights[row][col])
            
        for col in range(COL):
            dfs(0, col, pacific, heights[0][col])
            dfs(ROW -1, col, atlantic, heights[ROW-1][col])
        
        for row in range(ROW):
            dfs(row, 0, pacific,heights[row][0])
            dfs(row, COL - 1, atlantic, heights[row][COL-1])
        
        result = list(pacific & atlantic)
        return [list(r) for r in result]
