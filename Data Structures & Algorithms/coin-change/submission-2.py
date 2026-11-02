class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [amount+1] * (amount+1)
        dp[0] = 0 
        for coin in coins:
            temp = [0] * (amount + 1)
            for curr in range(amount+1):
                skip = dp[curr]
                include = amount + 1
                if curr >= coin:
                    include = 1 + temp[curr - coin]
                temp[curr] = min(skip, include)
            dp = temp
        if dp[amount] == amount+1: return -1
        return dp[amount]

                


        
        