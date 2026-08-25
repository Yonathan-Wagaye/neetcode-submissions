"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node

        
        queue = deque([node])
        cloned = {}
        visited = set()
        
        while queue:
            n = len(queue)
            copyNode = None
            for i in range(n):
                currentNode = queue.popleft()
                visited.add(currentNode.val)
                if currentNode.val not in cloned:
                    copyNode = Node(currentNode.val)
                    cloned[currentNode.val] = copyNode
                else:
                    copyNode = cloned[currentNode.val]

                

                neighborNode = None
                for neighbor in currentNode.neighbors:
                    if neighbor.val not in cloned:
                        neighborNode = Node(neighbor.val)
                        cloned[neighbor.val] = neighborNode
                    else:
                        neighborNode = cloned[neighbor.val]
                    copyNode.neighbors.append(neighborNode)
                    
                    if neighbor.val not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor.val)
                        
        return cloned[1]
                    
        