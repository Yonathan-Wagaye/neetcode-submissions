from collections import Counter

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        freq  = [Counter(binary) for binary in strs] # {'0': 0, '1': 0}
        print(freq)
        cache = {}
        N = len(strs)
        def dfs(index, n, m):
            if index>=N:
                return 0
            if (index, n, m) in cache:
                return cache[(index, n, m)]
            zeroCount, oneCount = freq[index]['0'], freq[index]['1']
            countWith = 0
            if n >= oneCount and m >= zeroCount:
                countWith =  1 + dfs(index+1, n-oneCount, m-zeroCount)
            countWithout = dfs(index+1, n, m)
            cache[(index, n, m)] = max(countWith, countWithout)
            return cache[(index, n, m)]

        return dfs(0, n, m) 
            
        