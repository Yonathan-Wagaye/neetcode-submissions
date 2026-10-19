class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(n)}

        for start, end in edges:
            adjList[start].append(end)
            adjList[end].append(start)

        visited = set()
        def dfs(node, prevNode):
            
            if node in visited:
                return False
            visited.add(node)
            children = adjList[node]
            for child in children:
                if child == prevNode:
                    continue
                if not dfs(child, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
       