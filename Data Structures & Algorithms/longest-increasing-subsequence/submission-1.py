class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}

        def findMaxLength(i):
            if i in cache:
                return cache[i]
            
            length = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    length = max(1 + findMaxLength(j), length)
            cache[i] = length
            return length
        return  max((findMaxLength(i) for i in range(n)), default=0)
