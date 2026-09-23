class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowMap = {}
        n = len(s)
        left = 0
        maxLength = 0
        for right in range(n):
            if s[right] not in windowMap: 
                windowMap[s[right]] = 1
            else: 
                windowMap[s[right]] += 1

            maxFreq = max(list(windowMap.values()))

            while (right-left + 1) - maxFreq > k:
                windowMap[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)    
        return maxLength
        