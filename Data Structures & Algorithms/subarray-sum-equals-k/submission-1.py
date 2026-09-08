class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        sumCount = {0: 1}
        totalCount = 0
        for num in nums:
            prefixSum += num

            if prefixSum - k in sumCount:
                totalCount+= sumCount[prefixSum - k]
            if prefixSum not in sumCount:
                sumCount[prefixSum] = 1
            else: sumCount[prefixSum] += 1

        return totalCount
            

        
        