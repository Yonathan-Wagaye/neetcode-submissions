class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)

        left, right = 0, n-1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        minIndex = left
        position  = [-1, -1]

        if nums[minIndex] <= target <= nums[n-1]: # target in right portion
            position[0] = minIndex
            position[1] = n - 1
        else: # target in left porition
            position[0] = 0
            position[1] = minIndex - 1

        left,right = position

        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return - 1
