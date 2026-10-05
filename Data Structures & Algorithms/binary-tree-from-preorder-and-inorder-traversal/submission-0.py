# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# inorder -> [i, j] where root is j//2 or j//2 + 1
# preorder -> [i, j] where root is i

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        preorder_index= 0
        inorderMap = { inorder[i] : i for i in range(n)}
        def rebuild(inStart, inEnd):
            nonlocal preorder_index
            if inStart >= inEnd: 
                return None
         
        
            root = TreeNode(preorder[preorder_index])
            preorder_index += 1
            inMid = inorderMap[root.val]
            root.left = rebuild(inStart, inMid)
            root.right = rebuild(inMid + 1, inEnd)
            return root

        return rebuild(0, n)
            



        

        