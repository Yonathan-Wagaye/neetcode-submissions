class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        n = len(s)
        def findWays(i, j):
            if s[i:j+1][0] == "0" or int(s[i:j+1]) > 26 or j >= n: return 0
            
            if j + 1 == n: return 1
            

            if (i, j) in cache:
                return cache[(i,j)]
            cache[(i,j)] = findWays(j+1, j+1) + findWays(j+1, j+2)
            return cache[(i,j)]
        
        return findWays(0,0) + findWays(0,1)
        