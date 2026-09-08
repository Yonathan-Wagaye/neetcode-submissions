class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return -1
        nums.append(0)
        nums.insert(0,0)
        n += 2
        prefix = [0]
        postfix = [0]
        for i in range(1, n):
            prefix.append(nums[i] + prefix[i-1])
            postfix.insert(0, nums[n-i-1] + postfix[-1 * i])
      
            
        for i in range(1, n-1):
            if prefix[i-1] == postfix[i+1]: 
                return i - 1
        return -1
