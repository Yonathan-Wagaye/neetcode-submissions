class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, 1
        n = len(nums)
        window = {nums[0]}

        while i < j and j < n:
            if j - i > k:
                window.remove(nums[i])
                i += 1
            if nums[j] in window: return True
            window.add(nums[j])
            j += 1
        return False
        