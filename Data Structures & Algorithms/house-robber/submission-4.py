class Solution:
        
    def rob(self, nums: List[int]) -> int:
        cache = {}
        n = len(nums)
        def robN(i):
            if i >= n:
                return 0
            elif i == n-1 or i == n-2:
                cache[i] = nums[i]
                return cache[i]
            elif i in cache:
                return cache[i]
            else:
                cache[i] = nums[i] + max(robN(i+2), robN(i+3))
                return cache[i]

        return max(robN(0),  robN(1)) 
  