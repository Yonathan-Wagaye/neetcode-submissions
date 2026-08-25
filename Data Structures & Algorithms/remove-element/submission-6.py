class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums) - 1
        while end >= 0:
            if nums[end] != val:
                break
            end -= 1
        current = end
        while current >= 0:
            if nums[current] == val:
                nums[current], nums[end] = nums[end], nums[current]
                end -= 1
            current -= 1
        return end + 1

    
            


        
        return left_pointer
        