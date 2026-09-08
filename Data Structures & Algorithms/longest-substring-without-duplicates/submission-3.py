class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1: return n
        left, right = 0, 1
        maxLength = 1
        visited = {s[0]: 0}

        while right < n:
            if s[right] in visited and left <= visited[s[right]]:
                left = visited[s[right]] + 1
            
            visited[s[right]] = right

            
            maxLength = max(maxLength, right - left + 1)
            right += 1

        return maxLength


                
            
