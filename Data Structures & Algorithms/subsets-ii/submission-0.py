class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        currSet = []
        nums.sort()
        n = len(nums)

        def dfs(i):
            if i == n:
                result.append(currSet.copy())
                return
            if i > n:
                return

            # include nums[i]
            currSet.append(nums[i])
            dfs(i+1)
            
            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
            
            # don't include any duplicate of nums[i]
            currSet.pop()
            dfs(i+1)
            return 
        dfs(0)
        return result

            
            