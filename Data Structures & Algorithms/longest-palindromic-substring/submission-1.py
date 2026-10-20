class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longestString = ''
        
        def getPalindorome(start, end, maxString):
            l, r = start, end
            currString = ''

            while l >= 0 and r < n and s[l] == s[r]:
                if r == l:
                    currString += s[l]
                else:
                    currString  = s[l] + currString + s[r]
                l -= 1
                r += 1

            if len(maxString) < len(currString):
                return currString
            return maxString
        
        for i in range(n):
            # even length
            longestString = getPalindorome(i,i, longestString)
            # odd length
            longestString = getPalindorome(i, i+1, longestString)
        
        return longestString
            
                
        