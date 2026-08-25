# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution:
    def __init__(self):
        self.balanced = True
    def findHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftHeight = 1 + self.findHeight(root.left)
        rightHeight = 1 + self.findHeight(root.right)
        if abs(leftHeight - rightHeight) > 1:
            self.balanced = False
        
        return max(leftHeight, rightHeight)
            
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height = self.findHeight(root)
        print(height)

        return self.balanced
            