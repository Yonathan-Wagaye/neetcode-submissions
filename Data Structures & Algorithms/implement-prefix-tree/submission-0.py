class TreeNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class PrefixTree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        # apple
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = TreeNode()

            currNode = currNode.children[char]
        currNode.endWord = True

    def search(self, word: str) -> bool:
        currNode = self.root
        for char in word:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return currNode.endWord
        
    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for char in prefix:
            if char not in currNode.children:
                return False
            currNode = currNode.children[char]
        return True
        