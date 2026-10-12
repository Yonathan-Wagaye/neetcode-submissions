class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char] 
        curr.isWord = True      

    def search(self, word: str) -> bool:
       
        def dfs(root, i):
            if i == len(word):
                return root.isWord

            if word[i] == '.':
                for char in root.children:
                    if dfs(root.children[char], i+1):
                        return True
                return False
            else:
                if word[i] not in root.children:
                    return False
                return dfs(root.children[word[i]], i+1)

        return dfs(self.root, 0)
            
        
