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

        
        
        oldToClone = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            currentNode = queue.popleft()
            for neighbor in currentNode.neighbors:
                if neighbor not in oldToClone:
                    oldToClone[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                oldToClone[currentNode].neighbors.append(oldToClone[neighbor])


        return oldToClone[node]
                    
        