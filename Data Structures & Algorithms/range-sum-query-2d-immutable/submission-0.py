class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.n, self.m = len(matrix), len(matrix[0])
        self.prefixSum = [[0] * (self.m + 1) for _ in range(self.n + 1)]

        for i in range(self.n):
            for j in range(self.m):
                if i == 0 and j == 0: self.prefixSum[i+1][i+1] = self.matrix[0][0]
                elif i == 0: self.prefixSum[i+1][j+1] = self.matrix[0][j] + self.prefixSum[1][j]
                elif j == 0: self.prefixSum[i+1][j+1] = self.matrix[i][0] + self.prefixSum[i][1]
                else:
                    self.prefixSum[i+1][j+1] = self.prefixSum[i][j+1] + self.prefixSum[i+1][j] - self.prefixSum[i][j] + self.matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2 = row1 + 1,col1 + 1,row2 + 1, col2 + 1
        return self.prefixSum[row2][col2] + self.prefixSum[row1-1][col1-1] - (self.prefixSum[row1-1][col2] + self.prefixSum[row2][col1 - 1])


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)