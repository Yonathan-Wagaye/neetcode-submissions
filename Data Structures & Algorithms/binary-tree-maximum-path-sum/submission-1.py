# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def dfs(root):
            nonlocal maxSum
            if not root:
                return 0

            leftSum = dfs(root.left)
            rightSum = dfs(root.right)
            splitSum = root.val + max(0, leftSum) + max(0, rightSum)
            nonSplitSum = root.val + max(0, leftSum, rightSum)
            maxSum = max(maxSum, splitSum, nonSplitSum)
            return nonSplitSum
        
        dfs(root)
        return maxSum
            

            
            

        