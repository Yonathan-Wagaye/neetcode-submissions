class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        result = []
        nums = sorted(nums)
        n = len(nums)
        def findSum(currIndex, remaining):
            if remaining == 0:
                result.append(path.copy())
                return

            if currIndex >= n or remaining < nums[currIndex]:
                return 
                 
            path.append(nums[currIndex])
            findSum(currIndex, remaining - nums[currIndex])  
            path.pop()
            findSum(currIndex + 1, remaining)
            return
        findSum(0, target)
        return result
            
            
            
        