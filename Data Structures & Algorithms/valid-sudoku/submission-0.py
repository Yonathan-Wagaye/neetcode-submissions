class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n, m = len(board), len(board[0])

        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(m)]
        grids = {(i,j):set() for i in range(n//3) for j in range(m//3)}
        
        for i in range(n):
            for j in range(m):     
                if board[i][j] != '.':
                    if int(board[i][j]) < 1 and int(board[i][j]) > 9: return False

                    if board[i][j] not in rows[i]: rows[i].add(board[i][j])
                    else: return False

                    if board[i][j] not in cols[j]: cols[j].add(board[i][j])
                    else: return False

                    if board[i][j] not in grids[(i//3, j//3)]: grids[(i//3, j//3)].add(board[i][j])
                    else: return False
        print(grids)
        return True
        