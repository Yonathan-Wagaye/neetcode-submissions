from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        freq  = [Counter(binary) for binary in strs]
        subSetCount = {}
        subSetCount[(m,n)] = 0
        maxCount = 0
        N = len(strs)

        for i in range(N):
            zeroCount, oneCount = freq[i]['0'], freq[i]['1']
            temp = subSetCount.copy()
            for zeros, ones in subSetCount:
                if zeroCount <= zeros and oneCount <= ones:
                    temp[(zeros-zeroCount, ones-oneCount)] = max(subSetCount[(zeros, ones)] + 1, temp.get((zeros-zeroCount, ones-oneCount), 0))
                
                    
            subSetCount = temp
        return max(subSetCount.values())
                
                
