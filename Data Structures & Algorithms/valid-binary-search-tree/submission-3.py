# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        interval = [float('-inf'), float('inf')]

        def dfs(root, interval):
            
            if not root: return True

            if interval[0] >= root.val or interval[1] <= root.val:
                return False

            left = dfs(root.left, [interval[0], root.val])

            # right traversal
            right = dfs(root.right, [root.val, interval[1]])

            return left and right

        return dfs(root, interval)


        