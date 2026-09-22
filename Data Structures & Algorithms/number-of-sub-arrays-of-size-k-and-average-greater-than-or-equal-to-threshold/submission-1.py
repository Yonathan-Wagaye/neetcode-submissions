class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left, right = 0, 1
        n = len(arr)
        windowSum = arr[0]
        
        subArrayCount = 0
        if  k == 1 and windowSum // k >= threshold: subArrayCount += 1
        while left < right and right < n:
            if right - left >= k: 
                windowSum -= arr[left]
                left += 1
            windowSum += arr[right]
            right += 1 
            if windowSum//k >= threshold and right - left == k:  
                subArrayCount += 1
                
        return subArrayCount


        