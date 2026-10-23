class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        half = sum(stones) // 2
        n = len(stones)
        cache = {}
        cache[half] = 0

        for i in range(n):
            temp = cache.copy()
            for capacity in cache:
                if stones[i] <= capacity:
                    temp[capacity - stones[i]] = max(temp.get(capacity-stones[i], 0), cache[capacity] + stones[i])
            cache = temp
        sack1 = max(cache.values())
        sack2 = sum(stones) - sack1
        return sack2 - sack1
        