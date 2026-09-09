class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        hashSet = set(nums)
        seqLength = []
        for num in nums:
            if num - 1 not in hashSet:
                curr = num
                currLength = 0
                while curr in hashSet:
                    curr += 1
                    currLength+= 1
                seqLength.append(currLength)
        return max(seqLength)



        