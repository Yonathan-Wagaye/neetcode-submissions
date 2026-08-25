# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.sortedArr = []
    def traverseInOrder(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self.traverseInOrder(root.left)
        self.sortedArr.append(root.val)
        self.traverseInOrder(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverseInOrder(root)
        return self.sortedArr[k-1]

        

        
        