class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        
        n = len(matrix[0]) 
        start = 0
        end = m - 1
        mid = (start + end) // 2
        possibleInner = mid

        while start <= end:
            if start == end:
                possibleInner = start
                start += 1
            elif matrix[mid][0] <= target <= matrix[mid][n-1]:
                possibleInner = mid
                break
            elif matrix[mid][0] > target:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start+end) // 2
        
        start = 0 
        end = n - 1
        mid = (start + end) // 2

        while start <= end:
            if matrix[possibleInner][mid] == target:
                return True
            elif matrix[possibleInner][mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end) // 2
        return False

            
            
