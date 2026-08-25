# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not p and not q: 
                return True
            elif not p or not q: 
                return False
            elif p.val != q.val: 
                return False

            return isSame(p.left, q.left) & isSame(p.right, q.right)

        def checkSubTree(root, subRoot):
            if not subRoot: 
                return True

            if not root: return False

                
            
            left = checkSubTree(root.left, subRoot)
            right = checkSubTree(root.right, subRoot)

            return isSame(root, subRoot) or left or right


        return checkSubTree(root, subRoot)
            

        