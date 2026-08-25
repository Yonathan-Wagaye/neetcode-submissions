class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []

        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else: hashMap[num] += 1
        
        def getMaxKey():
            maxKey = list(hashMap.keys())[0]
            for elt in hashMap:
                if hashMap[maxKey] < hashMap[elt]:
                    maxKey = elt
            return maxKey

        result = []
        for i in range(k):
            maxKey = getMaxKey()
            hashMap.pop(maxKey)
            result.append(maxKey)

        return result