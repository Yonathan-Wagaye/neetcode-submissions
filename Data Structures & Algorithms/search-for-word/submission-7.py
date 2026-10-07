class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = set()
        l = len(word)
        wl = len(word)
        def dfs(rowVec, colVec, k):
            if min(rowVec, colVec) < 0 or rowVec >= row or colVec >= col or (rowVec, colVec) in visited or board[rowVec][colVec] != word[k]: 
                return False 
            
            if k == wl - 1: return True

            visited.add((rowVec, colVec))
            found = (
                dfs(rowVec + 1, colVec, k + 1) or
                dfs(rowVec - 1, colVec, k + 1) or
                dfs(rowVec, colVec+ 1, k + 1) or
                dfs(rowVec, colVec - 1, k + 1)
            )
            visited.remove((rowVec, colVec))
            return found
        
        for i in range(row):
            for j in range(col):
                if dfs(i,j, 0):
                    return True
        return False