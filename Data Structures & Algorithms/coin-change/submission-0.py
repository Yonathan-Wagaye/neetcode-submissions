class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        cache = {}
        

        def countChange(leftOver):
            if leftOver == 0:
                return 0
            if leftOver < 0:
                return float('inf')
            
            if leftOver in cache:
                return cache[leftOver]

            minCount = float('inf')

            for coin in coins:   
                count = 1 + countChange(leftOver-coin)
                minCount = min(minCount, count)
            
            cache[leftOver] = minCount
            return minCount

        result = countChange(amount)
        if result == float('inf'): return -1
        return result
                
            
            
                

        