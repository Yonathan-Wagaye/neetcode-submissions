# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.currentSum = 0
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False

        self.currentSum += root.val
        if root.left == None and root.right == None:
            if self.currentSum == targetSum: return True
            else:
                self.currentSum -= root.val
                return False

            
        
        if self.hasPathSum(root.left, targetSum):
            return True


        if self.hasPathSum(root.right, targetSum):
            return True

        self.currentSum -= root.val

        
        return False