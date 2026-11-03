class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[amount] = 1

        for j in range(n-1, -1, -1):
            temp = [0] * (amount + 1)
            temp[amount] = 1
            for i in range(amount - 1, -1, -1):
                if i + coins[j] <= amount:
                    temp[i] = temp[i+ coins[j]] + dp[i]
                else:
                   temp[i] = dp[i]
            dp = temp
        return dp[0]

        