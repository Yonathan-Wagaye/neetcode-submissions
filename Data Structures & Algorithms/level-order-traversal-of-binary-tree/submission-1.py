# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodeDeque = deque([root])
        levels = []

        while len(nodeDeque) > 0:
            currentLevel = []
        
            for i in range(len(nodeDeque)):
                currentNode = nodeDeque.popleft()
                currentLevel.append(currentNode.val)
                if currentNode.left:
                    nodeDeque.append(currentNode.left)
                if currentNode.right:
                    nodeDeque.append(currentNode.right)
                
                
            levels.append(currentLevel)
        return levels
                
        