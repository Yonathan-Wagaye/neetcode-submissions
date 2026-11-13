class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goalPost = n-1

        currentPost = n-2
        while currentPost >= 0:
            if currentPost + nums[currentPost] >= goalPost:
                goalPost = currentPost
            currentPost -= 1
        return goalPost == 0


        