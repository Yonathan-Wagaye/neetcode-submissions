class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0

        maxSum = nums[0]
        currSum = nums[0]

        for i in range(1, len(nums)):
            currSum = max(0, currSum) + nums[i]
            maxSum = max(maxSum, currSum)
        return maxSum
        