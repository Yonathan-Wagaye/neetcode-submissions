class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        half = sum(stones) // 2
        print(half)
        n = len(stones)
        cache = {}
        def packStone(i, capacity):
            if i >= n or capacity <= 0:
                return 0
            
            if (i,capacity) in cache:
                return cache[(i, capacity)]
            withStone = 0
            if capacity >= stones[i]:
                withStone = stones[i] + packStone(i+1, capacity - stones[i])
            withoutStone = packStone(i+1, capacity)
            cache[(i, capacity)] = max(withStone, withoutStone)

            return cache[(i, capacity)]
        sack1 = packStone(0, half)
        sack2 = sum(stones) - sack1
        return sack2 - sack1
            
            
        