class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n,m = len(profit), capacity

        cache = [0] * (m+1) 

        for i in range(n):
            currRow = [0] * (m+1)
            for c in range(1, m+1):
                skip = cache[c]
                include = 0
                if weight[i] <= c:
                    include = profit[i] + currRow[c-weight[i]]
                currRow[c] = max(include, skip)
            cache = currRow
        return cache[m]

            
