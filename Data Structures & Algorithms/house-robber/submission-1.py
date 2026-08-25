class Solution:
    
    def startFromN(self, nums, cache, n):
        print(f"Calculating rob {n} with cache {cache}")
        if n >= len(nums):
            return 0
        if n in cache:
            return cache[n]

        maxValue = 0
        currentValue = None
        for i in range(n+2, len(nums)):
            if i in cache:
                currentValue = cache[i]
            else:
                currentValue = self.startFromN(nums, cache, i)
            if currentValue > maxValue:
                maxValue = currentValue
        cache[n] = nums[n] + maxValue
        return cache[n]

        
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        cache = {}
        return max(self.startFromN(nums, cache, 0), self.startFromN(nums, cache, 1))
  