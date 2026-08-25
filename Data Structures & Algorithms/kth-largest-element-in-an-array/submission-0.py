import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)

        kLargest = nums[0]

        for i in range(k):
            kLargest = heapq.heappop_max(nums)
        
        return kLargest