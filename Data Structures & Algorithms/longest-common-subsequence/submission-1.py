class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1), len(text2)
        grid = {}

        def lcsDfs(i, j):
            if i >= n or j >= m:
                return 0

            elif (i,j) in grid:
                return grid[(i,j)]
            
            else:
                if text1[i] == text2[j]:
                    grid[(i, j)] = 1 + lcsDfs(i+1, j+1)
                    return grid[(i,j)]

                else:
                    grid[(i,j)] = max(lcsDfs(i+1, j) , lcsDfs(i, j+1))
                    return grid[(i,j)]
        return lcsDfs(0,0)
