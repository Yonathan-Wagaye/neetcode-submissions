# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return -1

        
            
            leftHeight = 1 + dfs(root.left)
            rightHeight = 1 + dfs(root.right)
            height = max(leftHeight, rightHeight)
            print(f"Height of {root.val} is {height}")
            print(f"Right height {rightHeight}, Left height {leftHeight}")
            possibleDiameter = leftHeight + rightHeight

            if self.diameter < possibleDiameter:
                self.diameter = possibleDiameter

            return height
    
        dfs(root)
        return self.diameter

        

        