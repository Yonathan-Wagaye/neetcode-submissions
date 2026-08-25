from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        count = defaultdict(list)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        
        def hashString(string):
            prod = 1

            for char in string:
                prod *= primes[ord(char) - ord('a')]
            return prod

        for string in strs:
            count[hashString(string)].append(string)
        return list(count.values())

        


