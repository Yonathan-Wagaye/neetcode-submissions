class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)

        if m == 0 or n == 0 or n < m: return ""
        
        windowMap, targetMap = {}, {}
        
        left, length = 0, n+1
        substring = ""

        for char in t:
            if char not in windowMap:
                windowMap[char] = 0

            if char not in targetMap: 
                targetMap[char] = 1
            else: targetMap[char] += 1
        
        windowCount, required = 0, len(targetMap)
        s += '-1'

        for right in range(n+1):
            while windowCount == required:
                currLen = right - left
                if currLen < length:
                    substring = s[left: right]
                    length = currLen
                if s[left] in windowMap:
                    if windowMap[s[left]] == targetMap[s[left]]: windowCount -= 1
                    windowMap[s[left]] -= 1
                left += 1

            if s[right] in windowMap:
                windowMap[s[right]] += 1
                if windowMap[s[right]] == targetMap[s[right]]: windowCount += 1
            else:
                if right == left:
                    left += 1
       
        return substring
                
                

                
                     