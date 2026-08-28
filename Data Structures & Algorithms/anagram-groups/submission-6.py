from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)
        for word in strs:
            chars = [0] * 26
            for char in word: 
                chars[ord(char)- ord('a')] += 1
            hashMap[tuple(chars)].append(word)

        return list(hashMap.values())