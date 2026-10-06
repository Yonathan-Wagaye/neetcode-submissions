# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ''
        def dfs(root):
            nonlocal res
            if not root:
                res += 'n,' 
                return
            res += f'{root.val},' 
            left = dfs(root.left)
            right = dfs(root.right)
            return 
        
        dfs(root)
        print(res)
        return res


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dataArray = data.split(',')
        index = 0 
        n = len(dataArray)
        
        
        def dfs():
            nonlocal index
            if index >= n:
                return None
            if dataArray[index] == 'n':
                index += 1
                return None
            
            root = TreeNode(int(dataArray[index]))
            index += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()
        
