class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {0:0, 1:0, 2:0}
        n = len(nums)
        for i in range(n):
            count[nums[i]] += 1
        
        k = 0
        for i in range(3):
            for j in range(count[i]):
                nums[k] = i
                k += 1
        return  nums
        