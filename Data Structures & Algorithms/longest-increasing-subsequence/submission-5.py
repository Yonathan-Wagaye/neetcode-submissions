class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[n-1] = 1

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(1, dp[i], dp[j] + 1)
                else:
                    dp[i] = max(1, dp[i]) 
        return max(dp)

        