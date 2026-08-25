class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n
        prevRow[n-1] = 1
        
        for i in range(m-1, -1, -1):   
            currRow = [0] * n
            currRow[n-1] = 1
            for j in range(n-2,  -1, -1):
                currRow[j] = prevRow[j] + currRow[j+1]
            prevRow = currRow
        return prevRow[0]



            
        