class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        count = {}
        
        for num in nums:
            if num not in count: count[num] = 1
            else: count[num] += 1
        n, m = len(count), len(nums)
        print(count)
        def dfs():
            if len(path) == m:
                result.append(path.copy())
                return

            for num in count:
                if count[num] <= 0: continue
                path.append(num)
                count[num] -= 1
                dfs()
                path.pop()
                count[num] += 1
            return 
        dfs()
        return result 
        