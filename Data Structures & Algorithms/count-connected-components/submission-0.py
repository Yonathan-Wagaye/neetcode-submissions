from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adjList = defaultdict(list)
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(node, prevNode):
            if node in visited:
                return 0
            
            visited.add(node)
            children = adjList[node]
            for child in children:
                if child == prevNode:
                    continue
                dfs(child, prevNode)
            return 1
        
        count = 0
        for node in range(n):
            count += dfs(node, -1)
        
        return count
        