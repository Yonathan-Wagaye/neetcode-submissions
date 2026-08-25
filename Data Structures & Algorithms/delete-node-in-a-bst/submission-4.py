# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        currNode = root
        while currNode.left:
            currNode = currNode.left
        return currNode

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            if root.val == key:
                if root.left and root.right:
                    minNode = self.findMin(root.right)
                    root.val = minNode.val
                    root.right = self.deleteNode(root.right, minNode.val)
                elif root.left:
                    return root.left
                else:
                    return root.right
            
            elif root.val > key:
                root.left = self.deleteNode(root.left, key)
            
            else:
                root.right = self.deleteNode(root.right, key)
        
        return root
