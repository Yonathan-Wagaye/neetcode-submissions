from collections import defaultdict
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        cache: defaultdict[tuple[int, int], int] = defaultdict(int)
        
        def countWays(currAmount, coinIndex):
            if currAmount == 0:
                return 1
            if coinIndex >= n or currAmount < 0:
                return 0
            
            if (currAmount, coinIndex) in cache:
                return cache[(currAmount, coinIndex)]
            
            count = 0 
            for i in range(coinIndex, n):
                count += countWays(currAmount - coins[i], i)
            cache[(currAmount, coinIndex)] = count
            return cache[(currAmount, coinIndex)]
        
        return countWays(amount, 0)
                

        