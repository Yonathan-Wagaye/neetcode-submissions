class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(n)}

        for start, end in edges:
            adjList[start].append(end)
        print(adjList)
        def dfs(node, visited):
            if node in visited:
                return False
            
            visited.add(node)  
            children = adjList[node]
            if children:
                for child in children:
                    if not dfs(child, visited):
                        return False
            return True

        for i in range(n):
            if not dfs(i, set()):
                return False

        for start, end in edges:
            adjList[end].append(start)
        
        visited = set()
        def isConnected(node):
            if node in visited:
                return
            
            visited.add(node)
            children = adjList[node]
            for child in children:
                isConnected(child)
            return 
        isConnected(0)
        return len(visited) == n