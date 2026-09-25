class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2: return 1
        left, right = 0, 0
        length = 0
    
        diff = 0

        for curr in range(1, n):
            currDiff = arr[right] - arr[curr]
            if currDiff == 0:
                left = curr
            elif diff != 0 and (currDiff < 0 and diff < 0) or (currDiff > 0 and diff > 0):
                left  = right
            diff = currDiff
            right += 1
            length = max(length, right - left + 1)
        return length

               

        
       
         


        
        