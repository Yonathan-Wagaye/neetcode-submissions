class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        n = len(nums)
        def walk(house):
            if house < 0:
                return 0

            elif house in cache:
                return cache[house]
            else:
                cache[house] = nums[house] + max(walk(house-2), walk(house-3))
                return cache[house]        
        return max(walk(n-1), walk(n-2))
        