class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        tCount = {}
        for sChar in s:
            if sChar not in sCount:
                sCount[sChar] = 1
            else:
                sCount[sChar] += 1
        for tChar in t:
            if tChar not in tCount:
                tCount[tChar] = 1
            else:
                tCount[tChar] += 1
        return sCount == tCount


        