class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1 and nums[0] == target:
            return 0
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        while start <= end:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: 
                start = mid + 1
            else:
                end = mid - 1
            mid = (start + end) // 2
        return -1

        