class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        bl, br = 0, 0            
        
        for i in range(n):
            for l,r in ((i,i), (i, i+1)):
                while l >= 0 and r < n and s[l] == s[r]:
                    if r - l + 1 > br - bl + 1:
                        bl,br = l,r
                    l -= 1
                    r += 1
        return s[bl:br+1]
            
                
        