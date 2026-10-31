class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}
        n = len(profit)

        def dfs(i, c):
            if c <= 0 or i >= n: return 0

            if (i,c) in cache: return cache[(i,c)]

            include = 0
            if weight[i] <= c :
                include = profit[i] + dfs(i, c-weight[i])
            exclude = dfs(i+1, c)
            cache[(i,c)] = max(include, exclude)
            return cache[(i,c)]
        
        return dfs(0, capacity)