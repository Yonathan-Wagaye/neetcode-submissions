class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        if n == 0:
            return [[]]
        elif n == 1:
            return [[], [nums[0]]]
        else:
            subsets_without = self.subsets(nums[1:])
            subsets_with = []
            for s in subsets_without:
                subsets_with.append([nums[0]] + s)
            return subsets_without + subsets_with