class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        cache = {} # (day, ticketBought)

        def findMinCost(dayIndex):
            if dayIndex >= n:
                return 0
            if dayIndex in cache:
                return cache[dayIndex]
            nextPossibleDay = dayIndex + 1
            minCost = float('inf')
            for i in range(3):
                if i == 1:
                    aWeekLater = days[dayIndex] + 6
                    while nextPossibleDay < n and days[nextPossibleDay] <= aWeekLater:
                        nextPossibleDay += 1
                elif i == 2:
                    aMonthLater = days[dayIndex] + 29
                    while nextPossibleDay < n and days[nextPossibleDay] <= aMonthLater:
                        nextPossibleDay += 1
                minCost = min(costs[i] + findMinCost(nextPossibleDay), minCost)
            cache[dayIndex] = minCost
            return cache[dayIndex]
        result = findMinCost(0)
        return result     