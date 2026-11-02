class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (n+1)

        costDuration = [(1, costs[0]), (7, costs[1]), (30, costs[2])]

        for i in range(n-1, -1, -1):
            minCost = float('inf')
            j = i
            for (duration, cost) in costDuration:   
                while j < n and days[j] < days[i] + duration:
                    j += 1
                minCost = min(minCost, cost + dp[j])
            dp[i] = minCost
        return dp[0]
    


        