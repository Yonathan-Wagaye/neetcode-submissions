class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        diffMap = {}
        for i in range(n):
            if nums[i] in diffMap:
                return [diffMap[nums[i]], i]
            diffMap[target-nums[i]] = i
        
        return []