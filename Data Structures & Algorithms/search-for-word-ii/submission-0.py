class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True
    
    def addArray(self, words):
        for word in words:
            self.add(word)
                


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROW, COL = len(board), len(board[0])
        result, visited = set(), set()

        trie = Trie()
        trie.addArray(words)

        def backtrack(row, col, node, word):
            if min(row, col) < 0 or row >= ROW or col >= COL or (row, col) in visited or board[row][col] not in node.children: 
                return 

            
            visited.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.isWord:
                result.add(word)

            
            dxns = [(0,1), (1, 0), (-1, 0), (0, -1)]
            for x,y in dxns:
                backtrack(row + x, col + y, node, word)
            visited.remove((row, col))
            return 
        
        for i in range(ROW):
            for j in range(COL):
                backtrack(i, j, trie.root, "")
                
        return list(result)

            