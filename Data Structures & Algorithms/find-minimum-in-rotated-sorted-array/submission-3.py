class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        minValue = nums[0]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                minValue = min(nums[left], minValue)
                left  = mid + 1
            else:
                minValue = min(nums[mid], minValue)
                right = mid - 1
    
        return minValue