from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sums = defaultdict(int)
        sums[(0,0)] = 1
        n = len(nums)
        for i in range(n):
            temp = defaultdict(int)
            for index, currSum in sums:
                temp[(i+1, currSum + nums[i])] += sums[(index, currSum)]
                temp[(i+1, currSum - nums[i])] += sums[(index, currSum)]
            sums = temp
        print(sums)
        return sums[(n,target)]

        