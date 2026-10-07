class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = set()
        l = len(word)
        def dfs(rowVec, colVec, pathWord):
            if (rowVec, colVec) in visited: return False
            if pathWord == word: return True
            if min(rowVec, colVec) < 0 or rowVec >= row or colVec >= col: return False 

            pl, wl = len(pathWord), len(word)
            minLen = min(pl, wl)
            if minLen > 0 and pathWord[minLen-1] != word[minLen-1]: return False

            # check if pathWord.length >= word.length
            
            pathWord += board[rowVec][colVec]
            visited.add((rowVec, colVec))

            left = dfs(rowVec, colVec+1, pathWord)
            if left: return True

            right = dfs(rowVec, colVec -1, pathWord)
            if right: return True

            down = dfs(rowVec+1, colVec, pathWord)
            if down: return True

            up = dfs(rowVec-1, colVec, pathWord)
            if up: return True

            visited.remove((rowVec, colVec))
            return False
        
        for i in range(row):
            for j in range(col):
                if dfs(i,j, ""):
                    return True
        return False