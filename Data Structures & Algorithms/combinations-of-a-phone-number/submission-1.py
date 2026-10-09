class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        letters = [letterMap[digit] for digit in digits]
        n = len(letters)

        curr = []
        result = []
        cIndex = 0

        def dfs(wIndex, cIndex):
            if wIndex == n:
                res = ''.join(curr)
                if res not in result: result.append(res)
                return
            if wIndex > n or cIndex >= len(letters[wIndex]):
                return
            i = 0
            while i < len(letters[wIndex]):
                curr.append(letters[wIndex][cIndex])
                dfs(wIndex+1, i)
                curr.pop()
                i += 1
            dfs(wIndex, cIndex + 1)   
            return 
        dfs(0, 0)
        if result and result[0] == "": return []
        return result
