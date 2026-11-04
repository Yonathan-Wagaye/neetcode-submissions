from collections import defaultdict
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxEnding, minEnding, best = nums[0], nums[0], nums[0]
        n = len(nums)

        for i in range(1, n):
            prevMax = maxEnding
            maxEnding = max(nums[i]*maxEnding, nums[i], nums[i]*minEnding)
            minEnding = min(nums[i]*prevMax, nums[i], nums[i]*minEnding)
            best = max(best, maxEnding)
            
        return best

            
            
        