class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        n = len(nums)
        cache =set()

        for i in range(n-1, -1, -1):
            if total//2 in cache: return True
            temp = set()
            for s in cache:
                temp.add(nums[i] + s)
            cache.add(nums[i])
            cache.update(temp)
        return False


        