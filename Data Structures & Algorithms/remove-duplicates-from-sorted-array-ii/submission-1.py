class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return nums
        topCount = 1
        curr, end = 1, 0
        def getCount():
            if nums[curr] == nums[end]: return topCount + 1
            else: return 1
        while curr < n:
            topCount = getCount()
            if topCount <= 2:
                if curr - end > 1:
                    nums[end+1], nums[curr] = nums[curr], nums[end+1]
                end += 1
            curr += 1 
        return end + 1
        