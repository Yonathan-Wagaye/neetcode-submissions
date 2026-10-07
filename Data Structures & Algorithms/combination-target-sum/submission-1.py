class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        result = []
        n = len(nums)
        def findSum(currIndex):
            if currIndex >= n:
                return
            if sum(path) > target:
                return
            
            path.append(nums[currIndex])
            if sum(path) == target:
                result.append(path.copy())
            elif sum(path) < target:
                findSum(currIndex)
            else:
                findSum(currIndex+1)  
            path.pop()
            findSum(currIndex + 1)
            return
        findSum(0)
        return result
            
            
            
        