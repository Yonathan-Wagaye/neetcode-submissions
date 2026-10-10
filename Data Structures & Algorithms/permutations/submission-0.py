class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        result = []
        for i in range(len(nums)):
            numsCpy = nums.copy()
            numsCpy.pop(i)
            withOut = self.permute(numsCpy)
            for elem in withOut:
                elem.insert(0, nums[i])
                result.append(elem)
        return result