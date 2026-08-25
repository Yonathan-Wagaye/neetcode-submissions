class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_index = 0
        for i in range(len(nums)):
            if nums[i] > nums[last_index]:
                nums[last_index+1], nums[i] = nums[i], nums[last_index+1]
                last_index+=1
        return last_index + 1 