class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = set()
        for num in nums:
            if num not in uniques: uniques.add(num)
            else: return True

        return False