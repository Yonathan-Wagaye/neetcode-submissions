class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2: return 1

        left = 0
        length = 0
        previousDiff = 0

        for right in range(1, n):
            currentDiff = arr[right - 1] - arr[right]

            if currentDiff == 0:
                left = right
            elif currentDiff * previousDiff > 0:
                left = right - 1
            previousDiff = currentDiff
            length = max(length, right - left + 1)
        return length

               

        
       
         


        
        