class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        cache = {}
        def jumpDfs(i):
            if i >= n:
                return False
            if i == n-1:
                return True
            if i in cache:
                return cache[i]
            
            for j in range(nums[i], 0, -1):
                if jumpDfs(i+j):
                    cache[i] = True
                    return cache[i]
            cache[i] = False
            return cache[i]
        
        return jumpDfs(0)
            

        