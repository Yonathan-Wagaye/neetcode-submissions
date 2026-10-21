class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        n = len(nums)
        cache = {}
        def dfs(i, currSum):
            if i >= n: return False
            if currSum == total//2: return True

            if (i, currSum) in cache: return cache[(i, currSum)]
            
            cache[(i,currSum)] = dfs(i+1, nums[i] + currSum) or dfs (i+1, currSum)
            return cache[(i,currSum)]
        
        return dfs(0, 0)
        