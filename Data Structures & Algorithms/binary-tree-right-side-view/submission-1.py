# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        nodeDeque = deque([root])
        visibleRight = []

        while nodeDeque:     
            visibleRight.append(nodeDeque[-1].val)
            n = len(nodeDeque)
            for i in range(n):
                currentNode = nodeDeque.popleft()
                if currentNode.left:
                    nodeDeque.append(currentNode.left)
                if currentNode.right:
                    nodeDeque.append(currentNode.right)
        return visibleRight
        
        