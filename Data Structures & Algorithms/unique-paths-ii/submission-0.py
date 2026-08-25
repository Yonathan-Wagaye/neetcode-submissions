class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = {}
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        def findPath(row, col):
            if row >= n or col >= m: return 0
            elif obstacleGrid[row][col] == 1: return 0
            elif row == n-1 and col == m-1: return 1
            elif (row, col) in cache: return cache[(row, col)]
            else:
                cache[(row, col)] = findPath(row + 1, col) + findPath(row, col + 1)
                return cache[(row, col)]
        return findPath(0, 0)


        