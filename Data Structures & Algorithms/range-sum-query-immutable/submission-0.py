class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0: self.prefixSum[0] = nums[i]
            else: self.prefixSum[i] = self.prefixSum[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        totalUntilRight = self.prefixSum[right]
        if left == 0: return totalUntilRight
        leftSum = self.prefixSum[left-1]

        return totalUntilRight - leftSum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)