class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums: return nums
        prefix = 1
        result = [1]
        n = len(nums)
        for i in range(1, n):
            prefix *= nums[i-1]
            result.append(prefix)
 
        postfix = nums[-1]
        for i in range(n-2, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result
        