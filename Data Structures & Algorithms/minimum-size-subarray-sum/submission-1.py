class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum = 0
        left, n = 0, len(nums)
        length = n + 1

        for right in range(n):
            currSum += nums[right]
            while currSum >= target:
                currSum -= nums[left]
                length = min(right - left + 1, length)
                left += 1 
        return 0 if length == n+1 else length
            

            
        