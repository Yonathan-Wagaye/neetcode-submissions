class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        n = len(nums)
        def dfs(i, target):
            if i == n and target == 0: return 1
            if i >= n: return 0

            if (i, target) in cache: return cache[(i,target)]

            cache[(i, target)] = dfs(i+1, target  + nums[i]) + dfs (i+1, target - nums[i])
            return cache[(i, target)]
        
        return dfs(0, target)

        